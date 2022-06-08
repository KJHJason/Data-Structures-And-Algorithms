"""
This Python script consists of a series of test cases for the various algorithms that
were implemented for this assignment. This program also compares various algorithms to each other
to demonstrate how fast they are.
"""

# import third party libraries
from colorama import Fore as F, init as coloramaInit

# import standard libraries
import random, re, platform, timeit, sys, datetime, pathlib
from typing import Union
sys.setrecursionlimit(1500) # if the program stops unexpectedly, lower the recursion limit

# import local python files
from functions import get_input, S_reset
from test_algorithms import merge_sort, quicksorts, bubble_sort, heap_sort, insertion_sort, intro_sort, \
                            intro_sort_modified, radix_sort, counting_sort, selection_sort, shellsort, tree_sort

SORTING_MENU = """
-------- Sorting Algorithms Test Menu --------

1. Test correctness of sorting algorithms
2. Test time taken to sort various arrays
X. Exit program

----------------------------------------------"""

NUM_REGEX = re.compile(r"^\d+$")
RANDOMNESS = 999999 # randint(0, RANDOMNESS) for generating an array of random numbers between 0 to RANDOMNESS
BASIC_SORT_LIMIT = 10000 # maximum number of elements in the array before testing bubble, selection, and insertion sort as they can take a long time

# logging keys for each sorting algorithms
BUBBLE_SORT = "Bubble sort"
SELECTION_SORT = "Selection sort"
INSERTION_SORT = "Insertion sort"
SHELL_SORT = "Shell sort"
HEAP_SORT = "Heap sort"
AVL_TREE_SORT = "AVL Tree sort"
MERGE_SORT = "Merge sort"
QUICK_SORT = "Quick sort"
THREE_WAY_QUICKSORT = "3-way quick sort"
INTRO_SORT = "Introsort"
MODIFIED_INTRO_SORT = "Modified Introsort"
COUNTING_SORT = "Counting sort"
RADIX_SORT = "Radix sort"
PYTHON_SORT = "Python's Timsort in C"

# for the various kind of tests
TEST1 = " (nearly sorted array)"
TEST2 = " (nearly sorted array, descending)"
TEST3 = " (random array)"
TEST4 = " (random array, descending)"
NUM_OF_TEST = 4

# Log file names for each test
PROGRAM_PATH = pathlib.Path(__file__).parent.absolute()
SORT_CORRECTNESS_LOG = "sorting_correctness"
SORT_TIME_LOG = "sorting_time"

# defines the results
CORRECT = "✓"
WRONG = "✗"
RECURSION_ERROR = "Recursion error: maximum recursion depth exceeded"

def get_nearly_sorted_array(n:int) -> list[int]:
    # 1 in n//2 chance of multiplying by 2 
    # (using not keyword to negate the boolean as if it is 0, it will be multiplied by 2)
    return [(1, 2)[not random.randint(0, (n -1)//2)] * i for i in range(n)]

def check_if_sorted(arr:list[int], reverse:bool=False) -> str:
    """
    Check if the array is sorted and returns a '✗' or '✓' depending on the result.
    """
    verdict = ""
    for i in range(0, len(arr)-1):
        if (reverse):
            if (arr[i] < arr[i+1]):
                verdict = WRONG
                break
        else:
            if (arr[i] > arr[i+1]):
                verdict = WRONG
                break

    if (verdict == ""):
        verdict = CORRECT

    return verdict

def get_arr_length() -> int:
    arrayLen = 0
    while (1):
        arrayLen = input("Enter the length of the array to test (F to cancel): ")
        if (arrayLen.strip().lower() == "f"):
            return "f"
        elif (NUM_REGEX.fullmatch(arrayLen)):
            arrayLen = int(arrayLen)
            if (arrayLen > 0):
                return arrayLen
            else:
                print(f"{F.LIGHTRED_EX}Please enter a number larger than 0...")
                S_reset(nl=True)
        else:
            print(f"{F.LIGHTRED_EX}Please enter a NUMBER that is larger than 0...")
            S_reset(nl=True)

def log_results(origFileName:str, results:dict[str: Union[float, str]], *args) -> None:
    """
    Logs the results of the tests
    """
    dateTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    readableDateTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    fileName = "".join([origFileName, "_", dateTime, ".log"])

    filePath = PROGRAM_PATH.joinpath("results_logs")

    if (origFileName == SORT_CORRECTNESS_LOG):
        filePath = filePath.joinpath("correctness-results")
    elif (origFileName == SORT_TIME_LOG):
        filePath = filePath.joinpath("time-results")

    filePath.mkdir(exist_ok=True, parents=True)
    filePath = filePath.joinpath(fileName)

    with open(filePath, "w", encoding="utf-8") as logFile:
        logFile.write(f"Logged at {readableDateTime}\n\n")

        for text in args:
            logFile.write(f"{text}\n")

        logFile.write("\n")

        counter = 0
        for test, result in results.items():
            logFile.write(f"{test}: {result}\n")
            counter += 1
            if (counter == NUM_OF_TEST):
                logFile.write("\n")
                counter = 0

    print(f"{F.LIGHTGREEN_EX}Results logged as {fileName}")
    S_reset()

def main() -> None:
    """
    This is the main function of the program. It is responsible for running the various test cases.
    """
    uInput = ""
    while (uInput != "x"):
        print(SORTING_MENU)
        uInput = get_input(prompt="Enter command: ", warning="Please enter a command from the menu above...", command=("1", "2", "x"))
        print()
        if (uInput == "x"):
            print(f"{F.LIGHTRED_EX}Thank you for using this program and have a nice day!")
            S_reset(nl=True)
            input("Please press ENTER to exit...")
        elif (uInput == "1"):
            # test correctness of sorting algorithms
            arrayLen = get_arr_length()
            if (arrayLen != "f"):
                arrOne = get_nearly_sorted_array(arrayLen)
                arrTwo = [random.randint(0, RANDOMNESS) for _ in range(arrayLen)]
                random.shuffle(arrTwo)
                print(f"\n{F.LIGHTYELLOW_EX}Testing correctness of sorting algorithms...")
                S_reset(nl=True)

                testHistory = {} # store the test results

                if (arrayLen <= BASIC_SORT_LIMIT):
                    # -------------------------------------------------------------------------------

                    print(f"{F.LIGHTYELLOW_EX}Testing bubble sort...")
                    S_reset()

                    testArr = arrOne.copy()
                    bubble_sort.bubble_sort(testArr)
                    verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                    print(f"Bubble sort (nearly sorted array): {verdict}")
                    testHistory[BUBBLE_SORT + TEST1] = verdict
                    del testArr

                    testArr = arrOne.copy()
                    bubble_sort.bubble_sort(testArr, reverse=True)
                    verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                    print(f"Bubble sort (nearly sorted array, descending): {verdict}\n")
                    testHistory[BUBBLE_SORT + TEST2] = verdict
                    del testArr

                    testArr = arrTwo.copy()
                    bubble_sort.bubble_sort(testArr)
                    verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                    print(f"Bubble sort (random array): {verdict}")
                    testHistory[BUBBLE_SORT + TEST3] = verdict
                    del testArr

                    testArr = arrTwo.copy()
                    bubble_sort.bubble_sort(testArr, reverse=True)
                    verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                    print(f"Bubble sort (random array, descending): {verdict}\n")
                    testHistory[BUBBLE_SORT + TEST4] = verdict
                    del testArr

                    # -------------------------------------------------------------------------------
                    
                    print(f"{F.LIGHTYELLOW_EX}Testing selection sort...")
                    S_reset()

                    testArr = arrOne.copy()
                    selection_sort.selection_sort(testArr)
                    verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                    print(f"Selection sort (nearly sorted array): {verdict}")
                    testHistory[SELECTION_SORT + TEST1] = verdict
                    del testArr

                    testArr = arrOne.copy()
                    selection_sort.selection_sort(testArr, reverse=True)
                    verdict = f"\t\t\t{check_if_sorted(testArr, reverse=True)}"
                    print(f"Selection sort (nearly sorted array, descending): {verdict}\n")
                    testHistory[SELECTION_SORT + TEST2] = verdict
                    del testArr
                    
                    testArr = arrTwo.copy()
                    selection_sort.selection_sort(testArr)
                    verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                    print(f"Selection sort (random array): {verdict}")
                    testHistory[SELECTION_SORT + TEST3] = verdict
                    del testArr

                    testArr = arrTwo.copy()
                    selection_sort.selection_sort(testArr, reverse=True)
                    verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                    print(f"Selection sort (random array, descending): {verdict}\n")
                    testHistory[SELECTION_SORT + TEST4] = verdict
                    del testArr

                    # -------------------------------------------------------------------------------
                    print(f"{F.LIGHTYELLOW_EX}Testing insertion sort...")
                    S_reset()

                    testArr = arrOne.copy()
                    insertion_sort.insertion_sort(testArr)
                    verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                    print(f"Insertion sort (nearly sorted array): {verdict}")
                    testHistory[INSERTION_SORT + TEST1] = verdict
                    del testArr

                    testArr = arrOne.copy()
                    insertion_sort.insertion_sort(testArr, reverse=True)
                    verdict = f"\t\t\t{check_if_sorted(testArr, reverse=True)}"
                    print(f"Insertion sort (nearly sorted array, descending): {verdict}\n")
                    testHistory[INSERTION_SORT + TEST2] = verdict
                    del testArr
                    
                    testArr = arrTwo.copy()
                    insertion_sort.insertion_sort(testArr)
                    verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                    print(f"Insertion sort (random array): {verdict}")
                    testHistory[INSERTION_SORT + TEST3] = verdict
                    del testArr

                    testArr = arrTwo.copy()
                    insertion_sort.insertion_sort(testArr, reverse=True)
                    verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                    print(f"Insertion sort (random array, descending): {verdict}\n")
                    testHistory[INSERTION_SORT + TEST4] = verdict
                    del testArr

                    # -------------------------------------------------------------------------------
                else:
                    print(f"{F.LIGHTRED_EX}Skipping bubble, insertion, and selection sort as it will take too long to sort...")
                    S_reset(nl=True)

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing shell sort (halving interval)...")
                S_reset()

                testArr = arrOne.copy()
                shellsort.shellsort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Shell sort (nearly sorted array): {verdict}")
                testHistory[SHELL_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                shellsort.shellsort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Shell sort (nearly sorted array, descending): {verdict}\n")
                testHistory[SHELL_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                shellsort.shellsort(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Shell sort (random array): {verdict}")
                testHistory[SHELL_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                shellsort.shellsort(testArr, reverse=True)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Shell sort (random array, descending): {verdict}\n")
                testHistory[SHELL_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing heap sort...")
                S_reset()

                testArr = arrOne.copy()
                heap_sort.heap_sort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Heap sort (nearly sorted array): {verdict}")
                testHistory[HEAP_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                heap_sort.heap_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Heap sort (nearly sorted array, descending): {verdict}\n")
                testHistory[HEAP_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                heap_sort.heap_sort(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Heap sort (random array): {verdict}")
                testHistory[HEAP_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                heap_sort.heap_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Heap sort (random array, descending): {verdict}\n")
                testHistory[HEAP_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing (AVL) tree sort...")
                S_reset()

                testArr = arrOne.copy()
                tree = tree_sort.AVLTree()
                tree.insert_array(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(tree.tree_sort())}"
                print(f"AVL Tree sort (nearly sorted array): {verdict}")
                testHistory[AVL_TREE_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                tree = tree_sort.AVLTree()
                tree.insert_array(testArr)
                verdict = f"\t\t\t{check_if_sorted(tree.tree_sort(reverse=True), reverse=True)}"
                print(f"AVL Tree sort (nearly sorted array, descending): {verdict}\n")
                testHistory[AVL_TREE_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                tree = tree_sort.AVLTree()
                tree.insert_array(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(tree.tree_sort())}"
                print(f"AVL Tree sort (random array): {verdict}")
                testHistory[AVL_TREE_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                tree = tree_sort.AVLTree()
                tree.insert_array(testArr)
                verdict = f"\t\t\t\t{check_if_sorted(tree.tree_sort(reverse=True), reverse=True)}"
                print(f"AVL Tree sort (random array, descending): {verdict}\n")
                testHistory[AVL_TREE_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing merge sort...")
                S_reset()

                testArr = arrOne.copy()
                merge_sort.merge_sort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Merge sort (nearly sorted array): {verdict}")
                testHistory[MERGE_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                merge_sort.merge_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Merge sort (nearly sorted array, descending): {verdict}\n")
                testHistory[MERGE_SORT + TEST2] = verdict
                del testArr
                
                testArr = arrTwo.copy()
                merge_sort.merge_sort(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Merge sort (random array): {verdict}")
                testHistory[MERGE_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                merge_sort.merge_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Merge sort (random array, descending): {verdict}\n")
                testHistory[MERGE_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing quick sort...")
                S_reset()

                verdict = "\t\t\t\t\t"
                try:
                    testArr = arrOne.copy()
                    quicksorts.quicksort(testArr)
                    verdict += check_if_sorted(testArr)
                    print(f"Quick sort (nearly sorted array): {verdict}")
                    testHistory[QUICK_SORT + TEST1] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (nearly sorted array): {verdict}Recursion error!")
                    S_reset()
                    testHistory[QUICK_SORT + TEST1] = verdict + RECURSION_ERROR

                verdict = "\t\t\t\t"
                try:
                    testArr = arrOne.copy()
                    quicksorts.quicksort(testArr, reverse=True)
                    verdict += check_if_sorted(testArr, reverse=True)
                    print(f"Quick sort (nearly sorted array, descending): {verdict}\n")
                    testHistory[QUICK_SORT + TEST2] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (nearly sorted array, descending): {verdict}Recursion error!")
                    S_reset(nl=True)
                    testHistory[QUICK_SORT + TEST2] = verdict + RECURSION_ERROR

                verdict = "\t\t\t\t\t\t"
                try:
                    testArr = arrTwo.copy()
                    quicksorts.quicksort(testArr)
                    verdict += check_if_sorted(testArr)
                    print(f"Quick sort (random array): {verdict}")
                    testHistory[QUICK_SORT + TEST3] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (random array): {verdict}Recursion error!")
                    S_reset()
                    testHistory[QUICK_SORT + TEST3] = verdict + RECURSION_ERROR

                verdict = "\t\t\t\t\t"
                try:
                    testArr = arrTwo.copy()
                    quicksorts.quicksort(testArr, reverse=True)
                    verdict += check_if_sorted(testArr, reverse=True)
                    print(f"Quick sort (random array, descending): {verdict}\n")
                    testHistory[QUICK_SORT + TEST4] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (random array, descending): {verdict}Recursion error!")
                    S_reset(nl=True)
                    testHistory[QUICK_SORT + TEST4] = verdict + RECURSION_ERROR

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing 3-way quick sort...")
                S_reset()

                verdict = "\t\t\t\t"
                try:
                    testArr = arrOne.copy()
                    quicksorts.three_way_quicksort(testArr)
                    verdict += check_if_sorted(testArr)
                    print(f"3-way Quick sort (nearly sorted array): {verdict}")
                    testHistory[THREE_WAY_QUICKSORT + TEST1] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way Quick sort (nearly sorted array): {verdict}Recursion error!")
                    S_reset()
                    testHistory[THREE_WAY_QUICKSORT + TEST1] = verdict + RECURSION_ERROR

                verdict = "\t\t\t"
                try:
                    testArr = arrOne.copy()
                    quicksorts.three_way_quicksort(testArr, reverse=True)
                    verdict += check_if_sorted(testArr, reverse=True)
                    print(f"3-way Quick sort (nearly sorted array, descending): {verdict}\n")
                    testHistory[THREE_WAY_QUICKSORT + TEST2] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way Quick sort (nearly sorted array, descending): {verdict}Recursion error!")
                    S_reset(nl=True)
                    testHistory[THREE_WAY_QUICKSORT + TEST2] = verdict + RECURSION_ERROR

                verdict = "\t\t\t\t\t"
                try:
                    testArr = arrTwo.copy()
                    quicksorts.three_way_quicksort(testArr)
                    verdict += check_if_sorted(testArr)
                    print(f"3-way Quick sort (random array): {verdict}")
                    testHistory[THREE_WAY_QUICKSORT + TEST3] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way Quick sort (random array): {verdict}Recursion error!")
                    S_reset()
                    testHistory[THREE_WAY_QUICKSORT + TEST3] = verdict + RECURSION_ERROR

                verdict = "\t\t\t\t"
                try:
                    testArr = arrTwo.copy()
                    quicksorts.three_way_quicksort(testArr, reverse=True)
                    verdict += check_if_sorted(testArr, reverse=True)
                    print(f"3-way Quick sort (random array, descending): {verdict}\n")
                    testHistory[THREE_WAY_QUICKSORT + TEST4] = verdict
                    del testArr
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way Quick sort (random array, descending): {verdict}Recursion error!")
                    S_reset(nl=True)
                    testHistory[THREE_WAY_QUICKSORT + TEST4] = verdict + RECURSION_ERROR

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing introsort...")
                S_reset()

                testArr = arrOne.copy()
                intro_sort.intro_sort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Introsort (nearly sorted array): {verdict}")
                testHistory[INTRO_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                intro_sort.intro_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Introsort (nearly sorted array, descending): {verdict}\n")
                testHistory[INTRO_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                intro_sort.intro_sort(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Introsort (random array): {verdict}")
                testHistory[INTRO_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                intro_sort.intro_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Introsort (random array, descending): {verdict}\n")
                testHistory[INTRO_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing introsort (modified using 3way quicksort)...")
                S_reset()

                testArr = arrOne.copy()
                intro_sort_modified.modified_intro_sort(testArr)
                verdict = f"\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Modified Introsort (nearly sorted array): {verdict}")
                testHistory[MODIFIED_INTRO_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                intro_sort_modified.modified_intro_sort(testArr, reverse=True)
                verdict = f"\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Modified  Introsort (nearly sorted array, descending): {verdict}\n")
                testHistory[MODIFIED_INTRO_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                intro_sort_modified.modified_intro_sort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Modified Introsort (random array): {verdict}")
                testHistory[MODIFIED_INTRO_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                intro_sort_modified.modified_intro_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Modified Introsort (random array, descending): {verdict}\n")
                testHistory[MODIFIED_INTRO_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing counting sort...")
                S_reset()

                testArr = arrOne.copy()
                counting_sort.counting_sort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Counting sort (nearly sorted array): {verdict}")
                testHistory[COUNTING_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                counting_sort.counting_sort(testArr, reverse=True)
                verdict = f"\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Counting sort (nearly sorted array, descending): {verdict}\n")
                testHistory[COUNTING_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                counting_sort.counting_sort(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Counting sort (random array): {verdict}")
                testHistory[COUNTING_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                counting_sort.counting_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Counting sort (random array, descending): {verdict}\n")
                testHistory[COUNTING_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing radix sort...")
                S_reset()

                testArr = arrOne.copy()
                radix_sort.radix_sort(testArr)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Radix sort (nearly sorted array): {verdict}")
                testHistory[RADIX_SORT + TEST1] = verdict
                del testArr

                testArr = arrOne.copy()
                radix_sort.radix_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Radix sort (nearly sorted array, descending): {verdict}\n")
                testHistory[RADIX_SORT + TEST2] = verdict
                del testArr

                testArr = arrTwo.copy()
                radix_sort.radix_sort(testArr)
                verdict = f"\t\t\t\t\t\t{check_if_sorted(testArr)}"
                print(f"Radix sort (random array): {verdict}")
                testHistory[RADIX_SORT + TEST3] = verdict
                del testArr

                testArr = arrTwo.copy()
                radix_sort.radix_sort(testArr, reverse=True)
                verdict = f"\t\t\t\t\t{check_if_sorted(testArr, reverse=True)}"
                print(f"Radix sort (random array, descending): {verdict}\n")
                testHistory[RADIX_SORT + TEST4] = verdict
                del testArr

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTGREEN_EX}All tests finished!")
                S_reset()

                testVerdict = ""
                recursionError = False
                for result in testHistory.values():
                    if (result.strip() != CORRECT and result.strip() != RECURSION_ERROR):
                        testVerdict = "error"
                        break
                    elif (result.strip() == RECURSION_ERROR):
                        recursionError = True

                if (testVerdict == "" and not recursionError):
                    print(f"{F.LIGHTGREEN_EX}Status: OK!")
                    S_reset()
                elif (testVerdict == "" and recursionError):
                    print(f"{F.LIGHTRED_EX}Status: FAILED DUE TO RECURSION ERROR!")
                    S_reset(nl=True)
                    logResultsInput = get_input(prompt=f"Would you like to log the results? (y/n): ", command=("y", "n"))
                    if (logResultsInput == "y"):
                        additionalTextHeader = "Additional information:\n"
                        additionalTextOne = "Nearly sorted array: \n" + str(arrOne) + "\n"
                        additionalTextTwo = "Randomised array:\n" + str(arrTwo)
                        log_results(SORT_CORRECTNESS_LOG, testHistory, additionalTextHeader, additionalTextOne, additionalTextTwo)
                    else:
                        print(f"{F.LIGHTYELLOW_EX}Results will not be logged.")
                        S_reset()
                else:
                    print(f"{F.LIGHTRED_EX}Status: FAILED, WILL BE LOGGED FOR DEBUGGING!")
                    S_reset()
                    additionalTextHeader = "Additional information:\n"
                    additionalTextOne = "Nearly sorted array: \n" + str(arrOne) + "\n"
                    additionalTextTwo = "Randomised array:\n" + str(arrTwo)
                    log_results(SORT_CORRECTNESS_LOG, testHistory, additionalTextHeader, additionalTextOne, additionalTextTwo)

        # -----------------------------------------------------------------------------------------------------------------------------------------------------

        elif (uInput == "2"):
            # test the time taken to sort
            arrayLen = get_arr_length()
            if (arrayLen != "f"):
                arrOne = get_nearly_sorted_array(arrayLen)
                arrTwo = [random.randint(0, RANDOMNESS) for _ in range(arrayLen)]
                random.shuffle(arrTwo)
                print(f"\n{F.LIGHTYELLOW_EX}Testing the time taken for each sorting algorithms to sort...")
                S_reset(nl=True)

                testResults = {}

                # --------------------------------------------------------------------------------------------

                if (arrayLen <= BASIC_SORT_LIMIT):
                    # --------------------------------------------------------------------------------------------

                    print(f"{F.LIGHTYELLOW_EX}Testing bubble sort...")
                    S_reset()
                    
                    testArr = arrOne.copy()
                    timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: bubble_sort.bubble_sort(testArr), number=1)}"
                    del testArr
                    print(f"Bubble sort (nearly sorted array): {timeTaken}")
                    testResults[BUBBLE_SORT + TEST1] = timeTaken

                    testArr = arrOne.copy()
                    timeTaken = f"\t\t\t\t{timeit.timeit(lambda: bubble_sort.bubble_sort(testArr, reverse=True), number=1)}"
                    print(f"Bubble sort (nearly sorted array, descending): {timeTaken}\n")
                    del testArr
                    testResults[BUBBLE_SORT + TEST2] = timeTaken

                    testArr = arrTwo.copy()
                    timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: bubble_sort.bubble_sort(testArr), number=1)}"
                    print(f"Bubble sort (random array): {timeTaken}")
                    del testArr
                    testResults[BUBBLE_SORT + TEST3] = timeTaken

                    testArr = arrTwo.copy()
                    timeTaken = f"\t\t\t\t{timeit.timeit(lambda: bubble_sort.bubble_sort(testArr, reverse=True), number=1)}"
                    print(f"Bubble sort (random array, descending): {timeTaken}\n")
                    del testArr
                    testResults[BUBBLE_SORT + TEST4] = timeTaken

                    # --------------------------------------------------------------------------------------------
                    
                    print(f"{F.LIGHTYELLOW_EX}Testing selection sort...")
                    S_reset()
                
                    testArr = arrOne.copy()
                    timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: selection_sort.selection_sort(testArr), number=1)}"
                    del testArr
                    print(f"Selection sort (nearly sorted array): {timeTaken}")
                    testResults[SELECTION_SORT + TEST1] = timeTaken

                    testArr = arrOne.copy()
                    timeTaken = f"\t\t\t{timeit.timeit(lambda: selection_sort.selection_sort(testArr, reverse=True), number=1)}"
                    print(f"Selection sort (nearly sorted array, descending): {timeTaken}\n")
                    del testArr
                    testResults[SELECTION_SORT + TEST2] = timeTaken

                    testArr = arrTwo.copy()
                    timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: selection_sort.selection_sort(testArr), number=1)}"
                    print(f"Selection sort (random array): {timeTaken}")
                    del testArr
                    testResults[SELECTION_SORT + TEST3] = timeTaken

                    testArr = arrTwo.copy()
                    timeTaken = f"\t\t\t\t{timeit.timeit(lambda: selection_sort.selection_sort(testArr, reverse=True), number=1)}"
                    print(f"Selection sort (random array, descending): {timeTaken}\n")
                    del testArr
                    testResults[SELECTION_SORT + TEST4] = timeTaken

                    # --------------------------------------------------------------------------------------------

                    print(f"{F.LIGHTYELLOW_EX}Testing insertion sort...")
                    S_reset()

                    testArr = arrOne.copy()
                    timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: insertion_sort.insertion_sort(testArr), number=1)}"
                    del testArr
                    print(f"Insertion sort (nearly sorted array): {timeTaken}")
                    testResults[INSERTION_SORT + TEST1] = timeTaken

                    testArr = arrOne.copy()
                    timeTaken = f"\t\t\t{timeit.timeit(lambda: insertion_sort.insertion_sort(testArr, reverse=True), number=1)}"
                    print(f"Insertion sort (nearly sorted array, descending): {timeTaken}\n")
                    del testArr
                    testResults[INSERTION_SORT + TEST2] = timeTaken

                    testArr = arrTwo.copy()
                    timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: insertion_sort.insertion_sort(testArr), number=1)}"
                    print(f"Insertion sort (random array): {timeTaken}")
                    del testArr
                    testResults[INSERTION_SORT + TEST3] = timeTaken

                    testArr = arrTwo.copy()
                    timeTaken = f"\t\t\t\t{timeit.timeit(lambda: insertion_sort.insertion_sort(testArr, reverse=True), number=1)}"
                    print(f"Insertion sort (random array, descending): {timeTaken}\n")
                    del testArr
                    testResults[INSERTION_SORT + TEST4] = timeTaken

                    # --------------------------------------------------------------------------------------------
                else:
                    print(f"{F.LIGHTRED_EX}Skipping bubble, insertion, and selection sort as it will take too long to sort...")
                    S_reset(nl=True)

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing shell sort (halving interval)...")
                S_reset()
                
                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: shellsort.shellsort(testArr), number=1)}"
                del testArr
                print(f"Shell sort (nearly sorted array): {timeTaken}")
                testResults[SHELL_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: shellsort.shellsort(testArr, reverse=True), number=1)}"
                print(f"Shell sort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[SHELL_SORT + TEST2] = timeTaken
            
                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: shellsort.shellsort(testArr), number=1)}"
                print(f"Shell sort (random array): {timeTaken}")
                del testArr
                testResults[SHELL_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: shellsort.shellsort(testArr, reverse=True), number=1)}"
                print(f"Shell sort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[SHELL_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing heap sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: heap_sort.heap_sort(testArr), number=1)}"
                del testArr
                print(f"Heap sort (nearly sorted array): {timeTaken}")
                testResults[HEAP_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: heap_sort.heap_sort(testArr, reverse=True), number=1)}"
                print(f"Heap sort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[HEAP_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: heap_sort.heap_sort(testArr), number=1)}"
                print(f"Heap sort (random array): {timeTaken}")
                del testArr
                testResults[HEAP_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: heap_sort.heap_sort(testArr, reverse=True), number=1)}"
                print(f"Heap sort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[HEAP_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing (AVL) tree sort...")
                S_reset()

                def test_tree_sort(arr:list[int], reverse:bool=False) -> None:
                    tree = tree_sort.AVLTree()
                    tree.insert_array(arr)
                    tree.tree_sort(reverse=reverse)

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: test_tree_sort(testArr), number=1)}"
                del testArr
                print(f"AVL tree sort (nearly sorted array): {timeTaken}")
                testResults[AVL_TREE_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t{timeit.timeit(lambda: test_tree_sort(testArr, reverse=True), number=1)}"
                print(f"AVL tree sort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[AVL_TREE_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: test_tree_sort(testArr), number=1)}"
                print(f"AVL tree sort (random array): {timeTaken}")
                del testArr
                testResults[AVL_TREE_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: test_tree_sort(testArr, reverse=True), number=1)}"
                print(f"AVL tree sort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[AVL_TREE_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing merge sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: merge_sort.merge_sort(testArr), number=1)}"
                del testArr
                print(f"Merge sort (nearly sorted array): {timeTaken}")
                testResults[MERGE_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: merge_sort.merge_sort(testArr, reverse=True), number=1)}"
                print(f"Merge sort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[MERGE_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: merge_sort.merge_sort(testArr), number=1)}"
                print(f"Merge sort (random array): {timeTaken}")
                del testArr
                testResults[MERGE_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: merge_sort.merge_sort(testArr, reverse=True), number=1)}"
                print(f"Merge sort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[MERGE_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing quick sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = "\t\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.quicksort(testArr), number=1))
                    del testArr
                    print(f"Quick sort (nearly sorted array): {timeTaken}")
                    testResults[QUICK_SORT + TEST1] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (nearly sorted array): {timeTaken}Recursion error!")
                    S_reset()
                    testResults[QUICK_SORT + TEST1] = timeTaken + RECURSION_ERROR

                testArr = arrOne.copy()
                timeTaken = "\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.quicksort(testArr, reverse=True), number=1))
                    del testArr
                    print(f"Quick sort (nearly sorted array, descending): {timeTaken}\n")
                    testResults[QUICK_SORT + TEST2] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (nearly sorted array, descending): {timeTaken}Recursion error!")
                    S_reset(nl=True)
                    testResults[QUICK_SORT + TEST2] = timeTaken + RECURSION_ERROR

                testArr = arrTwo.copy()
                timeTaken = "\t\t\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.quicksort(testArr), number=1))
                    del testArr
                    print(f"Quick sort (random array): {timeTaken}")
                    testResults[QUICK_SORT + TEST3] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}Quick sort (random array): {timeTaken}Recursion error!")
                    S_reset()
                    testResults[QUICK_SORT + TEST3] = timeTaken + RECURSION_ERROR

                testArr = arrTwo.copy()
                timeTaken = "\t\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.quicksort(testArr, reverse=True), number=1))
                    del testArr
                    print(f"Quick sort (random array, descending): {timeTaken}\n")
                    testResults[QUICK_SORT + TEST4] = timeTaken
                except (RecursionError):    
                    print(f"{F.LIGHTRED_EX}Quick sort (random array, descending): {timeTaken}Recursion error!")
                    S_reset(nl=True)
                    testResults[QUICK_SORT + TEST4] = timeTaken + RECURSION_ERROR

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing 3-way quick sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = "\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr), number=1))
                    del testArr
                    print(f"3-way quick sort (nearly sorted array): {timeTaken}")
                    testResults[THREE_WAY_QUICKSORT + TEST1] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way quick sort (nearly sorted array): {timeTaken}Recursion error!")
                    S_reset()
                    testResults[THREE_WAY_QUICKSORT + TEST1] = timeTaken + RECURSION_ERROR

                testArr = arrOne.copy()
                timeTaken = "\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr, reverse=True), number=1))
                    del testArr
                    print(f"3-way quick sort (nearly sorted array, descending): {timeTaken}\n")
                    testResults[THREE_WAY_QUICKSORT + TEST2] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way quick sort (nearly sorted array, descending): {timeTaken}Recursion error!")
                    S_reset(nl=True)
                    testResults[THREE_WAY_QUICKSORT + TEST2] = timeTaken + RECURSION_ERROR

                testArr = arrTwo.copy()
                timeTaken = "\t\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr), number=1))
                    del testArr
                    print(f"3-way quick sort (random array): {timeTaken}")
                    testResults[THREE_WAY_QUICKSORT + TEST3] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way quick sort (random array): {timeTaken}Recursion error!")
                    S_reset()
                    testResults[THREE_WAY_QUICKSORT + TEST3] = timeTaken + RECURSION_ERROR

                testArr = arrTwo.copy()
                timeTaken = "\t\t\t\t"
                try:
                    timeTaken += str(timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr, reverse=True), number=1))
                    del testArr
                    print(f"3-way quick sort (random array, descending): {timeTaken}\n")
                    testResults[THREE_WAY_QUICKSORT + TEST4] = timeTaken
                except (RecursionError):
                    print(f"{F.LIGHTRED_EX}3-way quick sort (random array, descending): {timeTaken}Recursion error!")
                    S_reset(nl=True)
                    testResults[THREE_WAY_QUICKSORT + TEST4] = timeTaken + RECURSION_ERROR

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing introsort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: intro_sort.intro_sort(testArr), number=1)}"
                print(f"Introsort (nearly sorted array): {timeTaken}")
                del testArr
                testResults[INTRO_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: intro_sort.intro_sort(testArr, reverse=True), number=1)}"
                print(f"Introsort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[INTRO_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: intro_sort.intro_sort(testArr), number=1)}"
                print(f"Introsort (random array): {timeTaken}")
                del testArr
                testResults[INTRO_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: intro_sort.intro_sort(testArr, reverse=True), number=1)}"
                print(f"Introsort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[INTRO_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing introsort (modified using 3way quicksort)...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr), number=1)}"
                print(f"Modified Introsort (nearly sorted array): {timeTaken}")
                del testArr
                testResults[MODIFIED_INTRO_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t{timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr, reverse=True), number=1)}"
                print(f"Modified Introsort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[MODIFIED_INTRO_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr), number=1)}"
                print(f"Modified Introsort (random array): {timeTaken}")
                del testArr
                testResults[MODIFIED_INTRO_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr, reverse=True), number=1)}"
                print(f"Modified Introsort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[MODIFIED_INTRO_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing counting sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: counting_sort.counting_sort(testArr), number=1)}"
                print(f"Counting sort (nearly sorted array): {timeTaken}")
                del testArr
                testResults[COUNTING_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t{timeit.timeit(lambda: counting_sort.counting_sort(testArr, reverse=True), number=1)}"
                print(f"Counting sort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[COUNTING_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: counting_sort.counting_sort(testArr), number=1)}"
                print(f"Counting sort (random array): {timeTaken}")
                del testArr
                testResults[COUNTING_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: counting_sort.counting_sort(testArr, reverse=True), number=1)}"
                print(f"Counting sort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[COUNTING_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing radix sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: radix_sort.radix_sort(testArr), number=1)}"
                print(f"Radix sort (nearly sorted array): {timeTaken}")
                del testArr
                testResults[RADIX_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: radix_sort.radix_sort(testArr, reverse=True), number=1)}"
                print(f"Radix sort (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[RADIX_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t\t{timeit.timeit(lambda: radix_sort.radix_sort(testArr), number=1)}"
                print(f"Radix sort (random array): {timeTaken}")    
                del testArr
                testResults[RADIX_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: radix_sort.radix_sort(testArr, reverse=True), number=1)}"
                print(f"Radix sort (random array, descending): {timeTaken}\n")
                del testArr
                testResults[RADIX_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing Python's built-in sort function...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = f"\t\t\t\t{timeit.timeit(lambda: testArr.sort(), number=1)}"
                print(f"Python's Timsort in C (nearly sorted array): {timeTaken}")
                del testArr
                testResults[PYTHON_SORT + TEST1] = timeTaken

                testArr = arrOne.copy()
                timeTaken = f"\t\t{timeit.timeit(lambda: testArr.sort(reverse=True), number=1)}"
                print(f"Python's Timsort in C (nearly sorted array, descending): {timeTaken}\n")
                del testArr
                testResults[PYTHON_SORT + TEST2] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t\t\t{timeit.timeit(lambda: testArr.sort(), number=1)}"
                print(f"Python's Timsort in C (random array): {timeTaken}")
                del testArr
                testResults[PYTHON_SORT + TEST3] = timeTaken

                testArr = arrTwo.copy()
                timeTaken = f"\t\t\t{timeit.timeit(lambda: testArr.sort(reverse=True), number=1)}"
                print(f"Python's Timsort in C (random array, descending): {timeTaken}\n")
                del testArr
                testResults[PYTHON_SORT + TEST4] = timeTaken

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTGREEN_EX}All tests finished!")
                S_reset()

                testVerdict = ""
                for result in testResults.values():
                    if ("error" in result):
                        testVerdict = "error"
                        break

                if (testVerdict == ""):
                    print(f"{F.LIGHTGREEN_EX}Status: OK!")
                else:
                    print(f"{F.LIGHTRED_EX}Status: FAILED!")
                S_reset()

                logResultsInput = get_input(prompt=f"Would you like to log the results? (y/n): ", command=("y", "n"))
                if (logResultsInput == "y"):
                    additionalTextHeader = "Additional information:\n"
                    additionalTextOne = "Nearly sorted array: \n" + str(arrOne) + "\n"
                    additionalTextTwo = "Randomised array:\n" + str(arrTwo)
                    log_results(SORT_TIME_LOG, testResults, additionalTextHeader, additionalTextOne, additionalTextTwo)
                else:
                    print(f"{F.LIGHTYELLOW_EX}Results will not be logged.")
                    S_reset()

if (__name__ == "__main__"):
    if (platform.system() == "Windows"):
        # colorama to escape the ANSI escape sequences for Windows systems.
        # Remove this block of code if it does not escape the ASNI escape sequences
        # as some Windows systems may have in-built support for it 
        # which can interfere with the colorama initialise function
        coloramaInit(autoreset=False, convert=True)

    main()