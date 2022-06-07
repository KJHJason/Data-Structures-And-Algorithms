"""
This Python script consists of a series of test cases for the various algorithms that
were implemented for this assignment. This program also compares various algorithms to each other
to demonstrate how fast they are.
"""

# import third party libraries
from colorama import Fore as F, init as coloramaInit

# import standard libraries
import random, re, platform, timeit, sys
sys.setrecursionlimit(1500)

# import local python files
from functions import get_input, S_reset
from test_algorithms import merge_sort, quicksorts, bubble_sort, heap_sort, insertion_sort, intro_sort, \
                            intro_sort_modified, radix_sort, selection_sort, shellsort, tree_sort

SORTING_MENU = """
-------- Sorting Algorithms Test Menu --------

1. Test correctness of sorting algorithms
2. Test time taken to sort various arrays
X. Exit program

----------------------------------------------"""

NUM_REGEX = re.compile(r"^\d+$")
RANDOMNESS = 99999 # randint(0, RANDOMNESS) for generating an array of random numbers between 0 to RANDOMNESS
BASIC_SORT_LIMIT = 10000 # maximum number of elements in the array before testing bubble, selection, and insertion sort as they can take a long time

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
                verdict = "✗"
                break
        else:
            if (arr[i] > arr[i+1]):
                verdict = "✗"
                break

    if (verdict == ""):
        verdict = "✓"

    return verdict

def get_arr_length() -> int:
    arrayLen = 0
    while (1):
        arrayLen = input("Enter the length of the array to test: ")
        if (NUM_REGEX.fullmatch(arrayLen)):
            arrayLen = int(arrayLen)
            if (arrayLen > 0):
                return arrayLen
            else:
                print(f"{F.LIGHTRED_EX}Please enter a number larger than 0...")
                S_reset(nl=True)
        else:
            print(f"{F.LIGHTRED_EX}Please enter a NUMBER that is larger than 0...")
            S_reset(nl=True)

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

            arrOne = get_nearly_sorted_array(arrayLen)
            arrTwo = [random.randint(0, RANDOMNESS) for _ in range(arrayLen)]
            random.shuffle(arrTwo)
            print(f"\n{F.LIGHTYELLOW_EX}Testing correctness of sorting algorithms...")
            S_reset(nl=True)

            testHistory = [] # store the test results

            if (arrayLen <= BASIC_SORT_LIMIT):
                # -------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing bubble sort...")
                S_reset()

                testArr = arrOne.copy()
                bubble_sort.bubble_sort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Bubble sort (nearly sorted array): {verdict}")
                testHistory.append(verdict)
                del testArr

                testArr = arrOne.copy()
                bubble_sort.bubble_sort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Bubble sort (nearly sorted array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr

                testArr = arrTwo.copy()
                bubble_sort.bubble_sort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Bubble sort (random array): {verdict}")
                testHistory.append(verdict)
                del testArr

                testArr = arrTwo.copy()
                bubble_sort.bubble_sort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Bubble sort (random array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr

                # -------------------------------------------------------------------------------
                
                print(f"{F.LIGHTYELLOW_EX}Testing selection sort...")
                S_reset()

                testArr = arrOne.copy()
                selection_sort.selection_sort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Selection sort (nearly sorted array): {verdict}")
                testHistory.append(verdict)
                del testArr

                testArr = arrOne.copy()
                selection_sort.selection_sort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Selection sort (nearly sorted array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr
                
                testArr = arrTwo.copy()
                selection_sort.selection_sort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Selection sort (random array): {verdict}")
                testHistory.append(verdict)
                del testArr

                testArr = arrTwo.copy()
                selection_sort.selection_sort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Selection sort (random array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr

                # -------------------------------------------------------------------------------
                print(f"{F.LIGHTYELLOW_EX}Testing insertion sort...")
                S_reset()

                testArr = arrOne.copy()
                insertion_sort.insertion_sort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Insertion sort (nearly sorted array): {verdict}")
                testHistory.append(verdict)
                del testArr

                testArr = arrOne.copy()
                insertion_sort.insertion_sort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Insertion sort (nearly sorted array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr
                
                testArr = arrTwo.copy()
                insertion_sort.insertion_sort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Insertion sort (random array): {verdict}")
                testHistory.append(verdict)
                del testArr

                testArr = arrTwo.copy()
                insertion_sort.insertion_sort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Insertion sort (random array, descending): {verdict}\n")
                testHistory.append(verdict)
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
            verdict = check_if_sorted(testArr)
            print(f"Shell sort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            shellsort.shellsort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Shell sort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            shellsort.shellsort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Shell sort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            shellsort.shellsort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Shell sort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing heap sort...")
            S_reset()

            testArr = arrOne.copy()
            heap_sort.heap_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Heap sort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            heap_sort.heap_sort(testArr, reverse=True)
            print(f"Heap sort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            heap_sort.heap_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Heap sort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            heap_sort.heap_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Heap sort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing (AVL) tree sort...")
            S_reset()

            testArr = arrOne.copy()
            tree = tree_sort.AVLTree()
            tree.insert_array(testArr)
            verdict = check_if_sorted(tree.tree_sort())
            print(f"Tree sort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            tree = tree_sort.AVLTree()
            tree.insert_array(testArr)
            verdict = check_if_sorted(tree.tree_sort(reverse=True), reverse=True)
            print(f"Tree sort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            tree = tree_sort.AVLTree()
            tree.insert_array(testArr)
            verdict = check_if_sorted(tree.tree_sort())
            print(f"Tree sort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            tree = tree_sort.AVLTree()
            tree.insert_array(testArr)
            verdict = check_if_sorted(tree.tree_sort(reverse=True), reverse=True)
            print(f"Tree sort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing merge sort...")
            S_reset()

            testArr = arrOne.copy()
            merge_sort.merge_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Merge sort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            merge_sort.merge_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Merge sort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr
            
            testArr = arrTwo.copy()
            merge_sort.merge_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Merge sort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            merge_sort.merge_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Merge sort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing quick sort...")
            S_reset()

            try:
                testArr = arrOne.copy()
                quicksorts.quicksort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Quick sort (nearly sorted array): {verdict}")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}Quick sort (nearly sorted array) failed due to recursion error...")
                S_reset()
                testHistory.append("✗")

            try:
                testArr = arrOne.copy()
                quicksorts.quicksort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Quick sort (nearly sorted array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}Quick sort (nearly sorted array, descending) failed due to recursion error...")
                S_reset(nl=True)
                testHistory.append("✗")

            try:
                testArr = arrTwo.copy()
                quicksorts.quicksort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"Quick sort (random array): {verdict}")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}Quick sort (random array) failed due to recursion error...")
                S_reset()
                testHistory.append("✗")

            try:
                testArr = arrTwo.copy()
                quicksorts.quicksort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"Quick sort (random array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}Quick sort (random array, descending) failed due to recursion error...")
                S_reset(nl=True)
                testHistory.append("✗")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing 3-way quick sort...")
            S_reset()

            try:
                testArr = arrOne.copy()
                quicksorts.three_way_quicksort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"3-way Quick sort (nearly sorted array): {verdict}")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}3-way Quick sort (nearly sorted array) failed due to recursion error...")
                S_reset()
                testHistory.append("✗")

            try:
                testArr = arrOne.copy()
                quicksorts.three_way_quicksort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"3-way Quick sort (nearly sorted array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}3-way Quick sort (nearly sorted array, descending) failed due to recursion error...")
                S_reset(nl=True)
                testHistory.append("✗")

            try:
                testArr = arrTwo.copy()
                quicksorts.three_way_quicksort(testArr)
                verdict = check_if_sorted(testArr)
                print(f"3-way Quick sort (random array): {verdict}")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}3-way Quick sort (random array) failed due to recursion error...")
                S_reset()
                testHistory.append("✗")

            try:
                testArr = arrTwo.copy()
                quicksorts.three_way_quicksort(testArr, reverse=True)
                verdict = check_if_sorted(testArr, reverse=True)
                print(f"3-way Quick sort (random array, descending): {verdict}\n")
                testHistory.append(verdict)
                del testArr
            except (RecursionError):
                print(f"{F.LIGHTRED_EX}3-way Quick sort (random array, descending) failed due to recursion error...")
                S_reset(nl=True)
                testHistory.append("✗")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing introsort...")
            S_reset()

            testArr = arrOne.copy()
            intro_sort.intro_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Introsort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            intro_sort.intro_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Introsort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            intro_sort.intro_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Introsort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            intro_sort.intro_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Introsort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing introsort (modified using 3way quicksort)...")
            S_reset()

            testArr = arrOne.copy()
            intro_sort_modified.modified_intro_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Modified Introsort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            intro_sort_modified.modified_intro_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Modified  Introsort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            intro_sort_modified.modified_intro_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Modified  Introsort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            intro_sort_modified.modified_intro_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Modified  Introsort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing radix sort...")
            S_reset()

            testArr = arrOne.copy()
            radix_sort.radix_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Radix sort (nearly sorted array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrOne.copy()
            radix_sort.radix_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Radix sort (nearly sorted array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            radix_sort.radix_sort(testArr)
            verdict = check_if_sorted(testArr)
            print(f"Radix sort (random array): {verdict}")
            testHistory.append(verdict)
            del testArr

            testArr = arrTwo.copy()
            radix_sort.radix_sort(testArr, reverse=True)
            verdict = check_if_sorted(testArr, reverse=True)
            print(f"Radix sort (random array, descending): {verdict}\n")
            testHistory.append(verdict)
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTGREEN_EX}All tests finished!")
            S_reset()
            if ("✗" in testHistory):
                print(f"{F.LIGHTRED_EX}Status: FAILED!")
            else:
                print(f"{F.LIGHTGREEN_EX}Status: OK!")
            S_reset()

        elif (uInput == "2"):
            # test the time taken to sort
            arrayLen = get_arr_length()

            arrOne = get_nearly_sorted_array(arrayLen)
            arrTwo = [random.randint(0, RANDOMNESS) for _ in range(arrayLen)]
            random.shuffle(arrTwo)
            print(f"\n{F.LIGHTYELLOW_EX}Testing the time taken for each sorting algorithms to sort...")
            S_reset(nl=True)

            testResults = []

            # --------------------------------------------------------------------------------------------

            if (arrayLen <= BASIC_SORT_LIMIT):
                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing bubble sort...")
                S_reset()
                
                testArr = arrOne.copy()
                timeTaken = timeit.timeit(lambda: bubble_sort.bubble_sort(testArr), number=1)
                del testArr
                print(f"Bubble sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
                testResults.append("✓")

                testArr = arrOne.copy()
                timeTaken = timeit.timeit(lambda: bubble_sort.bubble_sort(testArr, reverse=True), number=1)
                print(f"Bubble sort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
                del testArr
                testResults.append("✓")

                testArr = arrTwo.copy()
                timeTaken = timeit.timeit(lambda: bubble_sort.bubble_sort(testArr), number=1)
                print(f"Bubble sort (random array): \t\t\t\t\t\t{timeTaken}")
                del testArr
                testResults.append("✓")

                testArr = arrTwo.copy()
                timeTaken = timeit.timeit(lambda: bubble_sort.bubble_sort(testArr, reverse=True), number=1)
                print(f"Bubble sort (random array, descending): \t\t\t\t{timeTaken}\n")
                del testArr
                testResults.append("✓")

                # --------------------------------------------------------------------------------------------
                
                print(f"{F.LIGHTYELLOW_EX}Testing selection sort...")
                S_reset()
            
                testArr = arrOne.copy()
                timeTaken = timeit.timeit(lambda: selection_sort.selection_sort(testArr), number=1)
                del testArr
                print(f"Selection sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
                testResults.append("✓")

                testArr = arrOne.copy()
                timeTaken = timeit.timeit(lambda: selection_sort.selection_sort(testArr, reverse=True), number=1)
                print(f"Selection sort (nearly sorted array, descending): \t\t\t{timeTaken}\n")
                del testArr
                testResults.append("✓")

                testArr = arrTwo.copy()
                timeTaken = timeit.timeit(lambda: selection_sort.selection_sort(testArr), number=1)
                print(f"Selection sort (random array): \t\t\t\t\t\t{timeTaken}")
                del testArr
                testResults.append("✓")

                testArr = arrTwo.copy()
                timeTaken = timeit.timeit(lambda: selection_sort.selection_sort(testArr, reverse=True), number=1)
                print(f"Selection sort (random array, descending): \t\t\t\t{timeTaken}\n")
                del testArr
                testResults.append("✓")

                # --------------------------------------------------------------------------------------------

                print(f"{F.LIGHTYELLOW_EX}Testing insertion sort...")
                S_reset()

                testArr = arrOne.copy()
                timeTaken = timeit.timeit(lambda: insertion_sort.insertion_sort(testArr), number=1)
                del testArr
                print(f"Insertion sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
                testResults.append("✓")

                testArr = arrOne.copy()
                timeTaken = timeit.timeit(lambda: insertion_sort.insertion_sort(testArr, reverse=True), number=1)
                print(f"Insertion sort (nearly sorted array, descending): \t\t\t{timeTaken}\n")
                del testArr
                testResults.append("✓")

                testArr = arrTwo.copy()
                timeTaken = timeit.timeit(lambda: insertion_sort.insertion_sort(testArr), number=1)
                print(f"Insertion sort (random array): \t\t\t\t\t\t{timeTaken}")
                del testArr
                testResults.append("✓")

                testArr = arrTwo.copy()
                timeTaken = timeit.timeit(lambda: insertion_sort.insertion_sort(testArr, reverse=True), number=1)
                print(f"Insertion sort (random array, descending): \t\t\t\t{timeTaken}\n")
                del testArr
                testResults.append("✓")

                # --------------------------------------------------------------------------------------------
            else:
                print(f"{F.LIGHTRED_EX}Skipping bubble, insertion, and selection sort as it will take too long to sort...")
                S_reset(nl=True)

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing shell sort (halving interval)...")
            S_reset()
            
            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: shellsort.shellsort(testArr), number=1)
            del testArr
            print(f"Shell sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: shellsort.shellsort(testArr, reverse=True), number=1)
            print(f"Shell sort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")
        
            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: shellsort.shellsort(testArr), number=1)
            print(f"Shell sort (random array): \t\t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: shellsort.shellsort(testArr, reverse=True), number=1)
            print(f"Shell sort (random array, descending): \t\t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing heap sort...")
            S_reset()

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: heap_sort.heap_sort(testArr), number=1)
            del testArr
            print(f"Heap sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: heap_sort.heap_sort(testArr, reverse=True), number=1)
            print(f"Heap sort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: heap_sort.heap_sort(testArr), number=1)
            print(f"Heap sort (random array): \t\t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: heap_sort.heap_sort(testArr, reverse=True), number=1)
            print(f"Heap sort (random array, descending): \t\t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing (AVL) tree sort...")
            S_reset()

            def test_tree_sort(arr:list[int], reverse:bool=False) -> None:
                tree = tree_sort.AVLTree()
                tree.insert_array(arr)
                tree.tree_sort(reverse=reverse)

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: test_tree_sort(testArr), number=1)
            del testArr
            print(f"AVL tree sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: test_tree_sort(testArr, reverse=True), number=1)
            print(f"AVL tree sort (nearly sorted array, descending): \t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: test_tree_sort(testArr), number=1)
            print(f"AVL tree sort (random array): \t\t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: test_tree_sort(testArr, reverse=True), number=1)
            print(f"AVL tree sort (random array, descending): \t\t\t\t{timeTaken}\n")
            del testArr

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing merge sort...")
            S_reset()

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: merge_sort.merge_sort(testArr), number=1)
            del testArr
            print(f"Merge sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: merge_sort.merge_sort(testArr, reverse=True), number=1)
            print(f"Merge sort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: merge_sort.merge_sort(testArr), number=1)
            print(f"Merge sort (random array): \t\t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: merge_sort.merge_sort(testArr, reverse=True), number=1)
            print(f"Merge sort (random array, descending): \t\t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing quick sort...")
            S_reset()

            testArr = arrOne.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.quicksort(testArr), number=1)
                del testArr
                print(f"Quick sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
                testResults.append("✓")
            except (RecursionError):
                print(f"Quick sort (nearly sorted array): \t\t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset()
                testResults.append("✗")

            testArr = arrOne.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.quicksort(testArr, reverse=True), number=1)
                del testArr
                print(f"Quick sort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
                testResults.append("✓")
            except (RecursionError):
                print(f"Quick sort (nearly sorted array, descending): \t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset(nl=True)
                testResults.append("✗")

            testArr = arrTwo.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.quicksort(testArr), number=1)
                del testArr
                print(f"Quick sort (random array): \t\t\t\t\t\t{timeTaken}")
                testResults.append("✓")
            except (RecursionError):
                print(f"Quick sort (random array): \t\t\t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset()
                testResults.append("✗")

            testArr = arrTwo.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.quicksort(testArr, reverse=True), number=1)
                del testArr
                print(f"Quick sort (random array, descending): \t\t\t\t\t{timeTaken}\n")
                testResults.append("✓")
            except (RecursionError):    
                print(f"Quick sort (random array, descending): \t\t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset(nl=True)
                testResults.append("✗")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing 3-way quick sort...")
            S_reset()

            testArr = arrOne.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr), number=1)
                del testArr
                print(f"3-way quick sort (nearly sorted array): \t\t\t\t{timeTaken}")
                testResults.append("✓")
            except (RecursionError):
                print(f"3-way quick sort (nearly sorted array): \t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset()
                testResults.append("✗")

            testArr = arrOne.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr, reverse=True), number=1)
                del testArr
                print(f"3-way quick sort (nearly sorted array, descending): \t\t\t{timeTaken}\n")
                testResults.append("✓")
            except (RecursionError):
                print(f"3-way quick sort (nearly sorted array, descending): \t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset(nl=True)
                testResults.append("✗")

            testArr = arrTwo.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr), number=1)
                del testArr
                print(f"3-way quick sort (random array): \t\t\t\t\t{timeTaken}")
                testResults.append("✓")
            except (RecursionError):
                print(f"3-way quick sort (random array): \t\t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset()
                testResults.append("✗")

            testArr = arrTwo.copy()
            try:
                timeTaken = timeit.timeit(lambda: quicksorts.three_way_quicksort(testArr, reverse=True), number=1)
                del testArr
                print(f"3-way quick sort (random array, descending): \t\t\t\t{timeTaken}\n")
                testResults.append("✓")
            except (RecursionError):
                print(f"3-way quick sort (random array, descending): \t\t\t\t{F.LIGHTRED_EX}Recursion error!")
                S_reset(nl=True)
                testResults.append("✗")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing introsort...")
            S_reset()

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: intro_sort.intro_sort(testArr), number=1)
            print(f"Introsort (nearly sorted array): \t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: intro_sort.intro_sort(testArr, reverse=True), number=1)
            print(f"Introsort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: intro_sort.intro_sort(testArr), number=1)
            print(f"Introsort (random array): \t\t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: intro_sort.intro_sort(testArr, reverse=True), number=1)
            print(f"Introsort (random array, descending): \t\t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing introsort (modified using 3way quicksort)...")
            S_reset()

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr), number=1)
            print(f"Modified Introsort (nearly sorted array): \t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr, reverse=True), number=1)
            print(f"Modified Introsort (nearly sorted array, descending): \t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr), number=1)
            print(f"Modified Introsort (modified using 3way quicksort) (random array): \t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: intro_sort_modified.modified_intro_sort(testArr, reverse=True), number=1)
            print(f"Modified Introsort (random array, descending): \t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing radix sort...")
            S_reset()

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: radix_sort.radix_sort(testArr), number=1)
            print(f"Radix sort (nearly sorted array): \t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: radix_sort.radix_sort(testArr, reverse=True), number=1)
            print(f"Radix sort (nearly sorted array, descending): \t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: radix_sort.radix_sort(testArr), number=1)
            print(f"Radix sort (random array): \t\t\t\t\t\t{timeTaken}")    
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: radix_sort.radix_sort(testArr, reverse=True), number=1)
            print(f"Radix sort (random array, descending): \t\t\t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTYELLOW_EX}Testing Python's built-in sort function...")
            S_reset()

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: testArr.sort(), number=1)
            print(f"Python's Timsort in C (nearly sorted array): \t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrOne.copy()
            timeTaken = timeit.timeit(lambda: testArr.sort(reverse=True), number=1)
            print(f"Python's Timsort in C (nearly sorted array, descending): \t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: testArr.sort(), number=1)
            print(f"Python's Timsort in C (random array): \t\t\t\t\t{timeTaken}")
            del testArr
            testResults.append("✓")

            testArr = arrTwo.copy()
            timeTaken = timeit.timeit(lambda: testArr.sort(reverse=True), number=1)
            print(f"Python's Timsort in C (random array, descending): \t\t\t{timeTaken}\n")
            del testArr
            testResults.append("✓")

            # --------------------------------------------------------------------------------------------

            print(f"{F.LIGHTGREEN_EX}All tests finished!")
            S_reset()
            if ("✗" in testResults):
                print(f"{F.LIGHTRED_EX}Status: FAILED!")
            else:
                print(f"{F.LIGHTGREEN_EX}Status: OK!")
            S_reset()

if (__name__ == "__main__"):
    if (platform.system() == "Windows"):
        # colorama to escape the ANSI escape sequences for Windows systems.
        # Remove this block of code if it does not escape the ASNI escape sequences
        # as some Windows systems may have in-built support for it 
        # which can interfere with the colorama initialise function
        coloramaInit(autoreset=False, convert=True)

    main()