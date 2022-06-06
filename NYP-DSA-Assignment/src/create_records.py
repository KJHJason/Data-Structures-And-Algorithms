"""
This file is not part of the main program.
However, it is used to generate nth number of records for testing purposes.
It can be used to see how long each sorting algorithm can take.

Run this Python script if you want to generate nth number of records for testing purposes.
"""

# import third-party libraries
from colorama import init as coloramaInit
from colorama import Fore as F

# import local python files
from hotel_record import HotelDatabase, NUM_REGEX
from functions import read_db_file, save_db_file, check_if_db_file_exists, get_input, shutdown, S_reset,\
                      preintialise_data, dbFileError

# import standard libraries
import re, platform, pathlib
from random import randint, uniform
from sys import exit as sysExit
from sys import exc_info

def main() -> int:
    """
    This program helps to generate nth number of records for testing purposes!
    """
    hotelDB = HotelDatabase()
    if (check_if_db_file_exists()):
        loadExisting = get_input(prompt="Load existing records? (y/n): ", command=("y", "n"))
        if (loadExisting == "y"):
            hotelDB = read_db_file(preintialiseData=False)
            print()
            if (len(hotelDB) == 0):
                print(f"{F.LIGHTRED_EX}No records found in the database!")
                S_reset(nl=True)
            else:
                print(f"{F.LIGHTGREEN_EX}Loaded {len(hotelDB)} records from the database!")
                S_reset(nl=True)
    else:
        print(f"{F.LIGHTRED_EX}No database file found. Creating new database file.")
        S_reset(nl=True)

    numOfRecords = 0
    while (1):
        numOfRecords = input("Enter the number of records to generate (x to cancel): ").strip()
        if (numOfRecords.lower() == "x"):
            print(f"{F.LIGHTRED_EX}Notice: No records generated!")
            S_reset()
            numOfRecords = 0
            break
        elif (re.fullmatch(NUM_REGEX, numOfRecords)):
            numOfRecords = int(numOfRecords)
            break
        else:
            print(f"{F.LIGHTRED_EX}Invalid input. Please enter a number.")
            S_reset(nl=True)

    for _ in range(numOfRecords):
        randPackage, randCust = preintialise_data()
        hotelDB.add_record(randPackage, randCust, randint(1,9), uniform(50,1000))

    save_db_file(hotelDB)
    return 0

if (__name__ == "__main__"):
    if (platform.system() == "Windows"):
        # colorama to escape the ANSI escape sequences for Windows systems.
        # Remove this block of code if it does not escape the ASNI escape sequences
        # as some Windows systems may have in-built support for it 
        # which can interfere with the colorama initialise function
        coloramaInit(autoreset=False, convert=True)

    try:
        print(f"{F.LIGHTYELLOW_EX}Welcome to the Hotel Records Generator meant for development use!")
        S_reset()
        print()
        main()
    except (KeyboardInterrupt, EOFError, dbFileError):
        pass
    except:
        print(f"{F.LIGHTRED_EX}Unexpected error caught: {exc_info()}")
        S_reset()
    finally:
        shutdown(nl=False, program=pathlib.Path(__file__).resolve().stem)
        sysExit(0)