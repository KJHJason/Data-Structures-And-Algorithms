"""
The main Python script for the assignment.

Run this file to run the main program!
"""

# import third-party libraries
from colorama import init as coloramaInit
from colorama import Fore as F

# import standard libraries
from sys import exit as sysExit
from sys import exc_info
import re, platform

# import local python files
from functions import S_reset, read_db_file, print_main_menu, print_sub_menu, get_input, log_error, \
                      countdown, shutdown, get_range, save_db_file, get_descending_flag, format_price, \
                      dbFileError
from hotel_record import print_record_data, NUM_REGEX, COST_REGEX

DEBUG_FLAG = False
PREINIT_TEN_RECORDS_FLAG = True
PANCAKE_MENU_HEADER = "Notice: You have opened the pancake sort menu!"

def main() -> None:
    hotelDB = read_db_file(preintialiseData=PREINIT_TEN_RECORDS_FLAG)
    uInput = ""
    while (uInput != "x"):
        print_main_menu(len(hotelDB), sortOrder=hotelDB.sort_order)
        uInput = get_input(prompt="Enter command: ", command=("1", "2", "3", "4", "5", "x"), warning="Invalid command input, please enter a valid command from the menu above...")

        if (uInput == "x"): 
            save_db_file(hotelDB)
            shutdown()

        elif (uInput == "1"):
            # display options
            if (len(hotelDB) < 1):
                print(f"{F.LIGHTRED_EX}Notice: There are no records to display...")
                S_reset(nl=True)
            else:
                subInput = ""
                while (subInput != "f"):
                    print_sub_menu(1)
                    subInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "4", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                    if (subInput == "1"):
                        # To satisfy basic function c.1
                        # display all records
                        print(hotelDB)
                    elif (subInput == "2"):
                        # To satisfy basic function c.7
                        # display records range from $X to $Y. e.g $100-200 (Not total cost 
                        # but the cost per pax range)
                        print()
                        while (1):
                            print("Please enter the range of cost per pax number you want to display in the format, $100-200...")
                            rangeInput = input("Enter the range of cost per pax number you want to display (x to cancel): $").lower().strip()
                            if (rangeInput == "x"):
                                break
                            formattedRange = get_range(rangeInput)
                            if (formattedRange == "error"):
                                print(f"{F.LIGHTRED_EX}Invalid range input, please enter in a \"$10-100\" format...")
                                S_reset(nl=True)
                            else:
                                hotelDB.search_for_range_of_cost(formattedRange[0], formattedRange[1])

                                searchAgainPrompt = get_input(prompt="Would you like to search again? (y/n): ", command=("y", "n"))
                                if (searchAgainPrompt == "n"):
                                    break
                                else:
                                    print()
                    elif (subInput == "3"):
                        # newly added
                        # search for records that matches the specified customer name
                        print()
                        searchAgainPrompt = ""
                        while (searchAgainPrompt != "x"):
                            custInp = input("Enter customer name (x to cancel): ").strip()

                            if (custInp == ""):
                                print(f"{F.LIGHTRED_EX}Error: Please provide a customer name...")
                                S_reset(nl=True)
                            elif (custInp.lower() != "x"):
                                success = hotelDB.search_for_customer(custInp, mode="Display")
                                if (success != -1):
                                    searchAgainPrompt = get_input(prompt="Would you like to search again? (y/n): ", command=("y", "n"))
                                    if (searchAgainPrompt == "n"):
                                        searchAgainPrompt = "x"
                            else:
                                searchAgainPrompt = "x"
                    elif (subInput == "4"):
                        # newly added
                        # search for records that matches the specified package name
                        print()
                        searchAgainPrompt = ""
                        while (searchAgainPrompt != "x"):
                            packageInput = input("Enter package name (x to cancel): ").strip()

                            if (packageInput == ""):
                                print(f"{F.LIGHTRED_EX}Error: Please provide a package name...")
                                S_reset(nl=True)
                            elif (packageInput.lower() != "x"):
                                success = hotelDB.search_for_package(packageInput, mode="Display")
                                if (success != -1):
                                    searchAgainPrompt = get_input(prompt="Would you like to search again? (y/n): ", command=("y", "n"))
                                    if (searchAgainPrompt == "n"):
                                        searchAgainPrompt = "x"
                            else:
                                searchAgainPrompt = "x"

        elif (uInput == "2"):
            # add new record (newly added)
            continueFlag = True
            while (continueFlag != False):
                packageName = customerName = ""
                paxNum = costperPax = 0

                print()
                while (continueFlag):
                    customerNameInput = input("Enter the customer name (F to cancel): ").lower().strip()
                    if (customerNameInput == "f"):
                        continueFlag = False
                        break
                    elif (customerNameInput == ""):
                        print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the customer name, \"{customerNameInput.title()}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            customerName = customerNameInput
                            print()
                            break
                    print()

                while (continueFlag):
                    packageNameInput = input("Enter the package name (F to cancel): ").lower().strip()
                    if (packageNameInput == "f"):
                        continueFlag = False
                        break
                    elif (packageNameInput == ""):
                        print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the package name, \"{packageNameInput.title()}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            packageName = packageNameInput
                            print()
                            break
                    print()

                while (continueFlag):
                    paxNumInput = input("Enter the number of pax (F to cancel): ").lower().strip()
                    if (paxNumInput == "f"):
                        continueFlag = False
                        break
                    elif (paxNumInput == ""):
                        print(f"{F.LIGHTRED_EX}Input cannot be empty, please enter a valid pax number of pax...")
                        S_reset()
                    elif (not re.fullmatch(NUM_REGEX, paxNumInput) or int(paxNumInput) < 1):
                        print(f"{F.LIGHTRED_EX}Invalid input, please enter a valid pax number of pax more than 0...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the number of pax, \"{paxNumInput}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            paxNum = paxNumInput
                            print()
                            break
                    print()

                while (continueFlag):
                    costperPaxInput = input("Enter the package cost per pax (F to cancel): $").lower().strip()
                    if (costperPaxInput == "f"):
                        continueFlag = False
                        break
                    elif (costperPaxInput == ""):
                        print(f"{F.LIGHTRED_EX}Package cost per pax cannot be empty, please enter a valid cost per pax...")
                        S_reset()
                    elif (not re.fullmatch(COST_REGEX, costperPaxInput)):
                        print(f"{F.LIGHTRED_EX}Invalid package cost per pax, please enter a valid cost per pax...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the package cost per pax, \"{format_price(costperPaxInput)}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            costperPax = costperPaxInput
                            print()
                            break
                    print()

                if (continueFlag):
                    print(print_record_data(packageName.title(), customerName.title(), paxNum, costperPax))
                    addConfirmation = get_input(prompt="Is this information correct? (y/n): ", command=("y", "n"), warning="Invalid confirmation input, please enter a valid confirmation command...")
                    if (addConfirmation == "y"):
                        hotelDB.add_record(packageName, customerName, paxNum, costperPax)
                        print(f"{F.LIGHTGREEN_EX}Record added successfully...")
                        S_reset()
                else:
                    print(f"\n{F.LIGHTRED_EX}Adding of record cancelled...")
                    S_reset()

        elif (uInput == "3"):
            # edit options
            if (len(hotelDB) < 1):
                print(f"{F.LIGHTRED_EX}Notice: There are no records to edit...")
                S_reset(nl=True)
            else:
                subInput = ""
                while (subInput != "f"):
                    print_sub_menu(3)
                    subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                    if (subInput == "1"):
                        # To satisfy basic function c.5
                        # Search record by Customer Name using Linear Search and update record
                        while (1):
                            customerName = input("Enter the customer name (F to cancel): ").lower().strip()
                            if (customerName == "f"):
                                break
                            elif (customerName == ""):
                                print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                                S_reset()
                            else:
                                hotelDB.search_for_customer(customerName, mode="Edit", bonus=False)

                    elif (subInput == "2"):
                        # To satisfy basic function c.6
                        # Search record by Package Name using Binary Search and update record
                        while (1):
                            packageName = input("Enter the package name (F to cancel): ").lower().strip()
                            if (packageName == "f"):
                                break
                            elif (packageName == ""):
                                print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                                S_reset()
                            else:
                                hotelDB.search_for_package(packageName, mode="Edit")

        elif (uInput == "4"):
            # sort options
            if (len(hotelDB) < 1):
                print(f"{F.LIGHTRED_EX}Notice: There are no records to sort...")
                S_reset(nl=True)
            else:
                subInput = ""
                while (subInput != "f"):
                    print_sub_menu(4)
                    subInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "4", "noob", "pancake", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                    if (subInput == "1"):
                        # sort by customer name using bubble sort
                        sortConfirmation = get_input(prompt="Do you want to sort the records by customer name? (y/n): ", command=("y", "n"))
                        if (sortConfirmation == "y"):
                            # To satisfy basic function c.2
                            hotelDB.sort_by_customer_name(get_descending_flag(nl=True), typeOfSort="bubble")

                    elif (subInput == "2"):
                        # To satisfy basic function c.3
                        # sort by package name using selection sort
                        sortConfirmation = get_input(prompt="Do you want to sort the records by package name? (y/n): ", command=("y", "n"))
                        if (sortConfirmation == "y"):
                            hotelDB.sort_by_package_name(get_descending_flag(nl=True))

                    elif (subInput == "3"):
                        # To satisfy basic function c.4
                        # sort by package cost using insertion sort
                        sortConfirmation = get_input(prompt="Do you want to sort the records by package cost? (y/n): ", command=("y", "n"))
                        if (sortConfirmation == "y"):
                            hotelDB.sort_by_package_cost(get_descending_flag(nl=True))

                    elif (subInput == "4"):
                        # newly added
                        # sort by package's number of pax using shellsort
                        sortConfirmation = get_input(prompt="Do you want to sort the records by pax number? (y/n): ", command=("y", "n"))
                        if (sortConfirmation == "y"):
                            hotelDB.sort_by_pax_num(get_descending_flag(nl=True))

                    # easter egg menu (newly added)
                    elif (subInput == "noob"):
                        print(f"\n{F.LIGHTYELLOW_EX}Notice: You have opened the easter egg menu!")
                        S_reset()
                        # sort by using a slow/non-sensical sorting algorithm such as bogosort
                        easterInput = ""
                        WarningMessage = f"{F.LIGHTRED_EX}Warning: This sorting algorithm is very SLOW and may take a long time to sort the records...\nPlease use with CAUTION, especially if you have a large number of records..."
                        while (easterInput != "q"):
                            print_sub_menu(6)
                            easterInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "4", "5", "6", "q"), warning="Invalid command input, please enter a valid option from the sub-menu above...")

                            if (easterInput == "1"):
                                # sort by customer name using stalin sort
                                WarningMessage = f"{F.LIGHTRED_EX}Warning: This sorting algorithm is fast when sorting the records...\nHowever, please use with CAUTION as it will result in DELETION of records that are not in the correct order..."
                                S_reset()

                                sortConfirmation = get_input(prompt="Do you want to sort the records by customer name? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.easter_egg_sorts(typeOfSort="stalinsort")
                            elif (easterInput == "2"):
                                # sort by package name using bogo sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by package name? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.easter_egg_sorts(typeOfSort="bogosort")
                            elif (easterInput == "3"):
                                # sort by package name using bozo sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by package name? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.easter_egg_sorts(typeOfSort="bozosort")
                            elif (easterInput == "4"):
                                # sort by package cost using slow sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by package cost? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.easter_egg_sorts(typeOfSort="slowsort")
                            elif (easterInput == "5"):
                                # sort by package's number of pax using sleep sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by pax number? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.easter_egg_sorts(typeOfSort="sleepsort")
                            elif (easterInput == "6"):
                                # sort by package's number of pax using gnome sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by pax number? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.easter_egg_sorts(typeOfSort="gnomesort")

                    elif (subInput == "pancake"):
                        # (newly added)
                        # another menu for sorting all types of records using pancake sort
                        # since I named this program the "Waffle Hotel Staycation Booking...",
                        # hence adding a dedicated menu for pancake sort as a joke
                        print(f"\n{F.LIGHTYELLOW_EX}{PANCAKE_MENU_HEADER}")
                        print(f"{'Here we offer pancakes in Waffle Hotel!':^{len(PANCAKE_MENU_HEADER)}}")
                        S_reset()

                        WarningMessage = f"{F.LIGHTRED_EX}Warning: This sorting algorithm is very SLOW and may take a long time to sort the records...\nPlease use with CAUTION, especially if you have a large number of records..."
                        pancakeInput = ""
                        while (pancakeInput != "q"):
                            print_sub_menu(7)
                            pancakeInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "4", "q"), warning="Invalid command input, please enter a valid pancake option from the sub-menu above...")
                            if (pancakeInput == "1"):
                                # sort by customer name using pancake sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by customer name? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.pancake_sort_records(mode="customerName")
                            elif (pancakeInput == "2"):
                                # sort by package name using pancake sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by package name? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.pancake_sort_records(mode="packageName")
                            elif (pancakeInput == "3"):
                                # sort by package cost using pancake sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by package cost? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.pancake_sort_records(mode="costPerPax")
                            elif (pancakeInput == "4"):
                                # sort by package's number of pax using pancake sort
                                sortConfirmation = get_input(prompt="Do you want to sort the records by pax number? (y/n): ", command=("y", "n"), prints=WarningMessage)
                                if (sortConfirmation == "y"):
                                    hotelDB.pancake_sort_records(mode="paxNum")

        elif (uInput == "5"):
            # delete options (newly added)
            if (len(hotelDB) < 1):
                print(f"{F.LIGHTRED_EX}Notice: There are no records to delete...")
                S_reset(nl=True)
            else:
                subInput = ""
                while (subInput != "f"):
                    print_sub_menu(5)
                    subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                    
                    if (subInput == "1"):
                        # Delete record by customer name
                        if (len(hotelDB) < 1):
                            print(f"{F.LIGHTRED_EX}Notice: There are no records to delete...")
                            S_reset(nl=True)
                        else:
                            while (1):
                                print()
                                customerName = input("Enter the customer name (F to cancel): ").lower().strip()
                                if (customerName == "f"):
                                    break
                                elif (customerName == ""):
                                    print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                                    S_reset()
                                else:
                                    hotelDB.search_for_customer(customerName, mode="Delete", bonus=True)
                                    if (len(hotelDB) < 1):
                                        break

                    elif (subInput == "2"):
                        # Delete record by package name
                        if (len(hotelDB) < 1):
                            print(f"{F.LIGHTRED_EX}Notice: There are no records to delete...")
                            S_reset(nl=True)
                        else:
                            while (1):
                                print()
                                packageName = input("Enter the package name (F to cancel): ").lower().strip()
                                if (packageName == "f"):
                                    break
                                elif (packageName == ""):
                                    print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                                    S_reset()
                                else:
                                    hotelDB.search_for_package(packageName, mode="Delete")
                                    if (len(hotelDB) < 1):
                                        break

if (__name__ == "__main__"):
    if (platform.system() == "Windows"):
        # colorama to escape the ANSI escape sequences for Windows systems.
        # Remove this block of code if it does not escape the ASNI escape sequences
        # as some Windows systems may have in-built support for it 
        # which can interfere with the colorama initialise function
        coloramaInit(autoreset=False, convert=True)

    if (not DEBUG_FLAG):
        try:
            main()
        except (KeyboardInterrupt, EOFError, dbFileError):
            shutdown(nl=True, abrupt=True)
        except:
            print()
            print(f"{F.LIGHTRED_EX}Unexpected error caught and all changes will be LOST:\n{exc_info()}")
            print(f"Please refer to the generated error log file for more details...")
            S_reset()
            log_error()
            print()
            countdown()
        finally:
            sysExit(0)
    else:
        main()