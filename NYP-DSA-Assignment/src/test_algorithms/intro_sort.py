# import standard libraries
from math import floor, log2

# import local python files
if (__package__ is None or __package__ == ''):
    from insertion_sort import insertion_sort
    from heap_sort import heap_sort
    from quicksorts import median_of_3, partition_to_2 as partition
else:
    from .insertion_sort import insertion_sort
    from .heap_sort import heap_sort
    from .quicksorts import median_of_3, partition_to_2 as partition

# define the maximum length of the array before using insertion sort
SIZE_THRESHOLD = 16 # if less than 16 elements, introsort will use insertion sort.
                    # I used the integer 16 as the threshold because GNU Standard C++ library also uses it;
                    # https://gcc.gnu.org/onlinedocs/gcc-12.1.0/libstdc++/api/a00650_source.html#l01838

def intro_sort(arr:list[int], reverse:bool=False) -> None:
    """
    Introsort or introspective sort is a hybrid sorting algorithm that consists of quick sort, 
    heap sort, and insertion sort.
    It is used in popular languages such as C++ which I have experience with. Hence, I wanted
    to implement std::sort(arr.begin(), arr.end()); in Python.
    
    By using a combination of these three sorting algorithms, introsort is able 
    to sort the array by package name in O(n log n) time for all best, worst, and average case 
    and eliminate quick sort's worst time complexity of O(n^2). 
    However, this algorithm is not stable due to the use of the quick sort algorithm.
    
    Why not just use heap sort?
    - Quick sort is actually faster than heap sort in most cases.
    - The disadvantage of quick sort is its worst time complexity of O(n^2)
    - Hence, introsort combines quick sort for its efficiency and 
      heap sort to avoid quick sort's worst time complexity of O(n^2)
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package name
    - reverse (bool): True if the array is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n log n)
    
    Space complexity: O(logn) for the heap sort on a sub-array of the array and call stack for quicksort
    
    More details:
    - https://en.wikipedia.org/wiki/Introsort
    
    When implementing this algorithm, I used the following references:
    Source code in C++:
    - https://gcc.gnu.org/onlinedocs/gcc-12.1.0/libstdc++/api/a00650_source.html

    Python implementation (which has some potential performance flaws):
    - https://github.com/TheAlgorithms/Python/blob/master/sorts/intro_sort.py

    Videos that explains the algorithm:
    - What Happens When You Call sort()? | Introsort Algorithm Explained
        - https://www.youtube.com/watch?v=MsvzXTXh0Jg&feature=youtu.be
    """
    if (not arr):
        # if array is empty, return
        return

    # calculate the max recursion depth of the algorithm for quick sort 
    # as to use heap sort when the max recursion depth has been reached
    # to avoid the worse case complexity of O(n^2) when using quick sort
    maxDepth = 2 * floor(log2(len(arr)))

    intro_sort_process(arr, 0, len(arr), maxDepth, reverse=reverse)

def intro_sort_process(arr:list[int], start:int, end:int, maxDepth:int, reverse:bool=False) -> None:
    """
    The main function that implements the introsort algorithm with reference to
    C++ Standard Library's std::sort();
    https://gcc.gnu.org/onlinedocs/gcc-12.1.0/libstdc++/api/a00650_source.html#l01908
    
    Requires 5 arguments:
    - arr (list): The array of elements to sort by package name
    - start (int): The starting index of the array
    - end (int): The lenght of the arrayy/highest index + 1
    - maxDepth (int): The max recursion depth of the algorithm before using heap sort
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    """
    while (end - start > SIZE_THRESHOLD):
        if (maxDepth == 0):
            # base case 1
            # start using heap sort on the sub-array if the max recursion depth is 0
            # as to avoid the worst case of O(n^2) when using quick sort
            arrCopy = arr[start:end+1]
            heap_sort(arrCopy, reverse=reverse)
            arr[start:end+1] = arrCopy
            return

        maxDepth -= 1

        # get the pivot for quick sort using the median of three concept
        pivot = median_of_3(arr, start, start + ((end - start) // 2), end - 1)

        # partition the array around the pivot
        partitionRes = partition(arr, start, end, pivot, reverse=reverse)

        # recursive case:
        # use the returned value from the partition function and recursively
        # sort the RIGHT side of the array by changing the start argument
        # to the returned value from the partition function
        intro_sort_process(arr, partitionRes, end, maxDepth, reverse=reverse)

        # change the end pointer to partitionRes after the recursive call process 
        # of sorting the right side of the array to sort the LEFT side of the array
        # in the next while loop iteration and start sorting the LEFT side of the array recursively
        end = partitionRes

    # base case 2
    # use insertion sort to sort the array/sub-array for smaller arrays as it is faster
    return insertion_sort(arr, startIdx=start, endIdx=end, reverse=reverse)

# test codes below
if (__name__ == "__main__"):
    import timeit, random, re

    NUM_REGEX = re.compile(r"\d+")

    def get_nearly_sorted_array(n:int) -> list:
        lengthOfPosibleValues = (n - 1) // 2
        possibility = [1 for _ in range(lengthOfPosibleValues)] + [2] # 1 in (n-1)/2 chance of multiplying by 2
        return [random.choice(possibility) * i for i in range(n)]

    def check_if_sorted(arr:list, reverse:bool=False, modelArr:list[int]=[]) -> int:
        """
        Check if the array is sorted
        """
        modelArr.sort(reverse=reverse)
        for i in range(0, len(arr)):
            if (arr[i] != modelArr[i]):
                return 0
        return 1

    # test the introsort algorithm
    numOfRecords = 0
    while (1):
        numOfRecords = input("Enter the number of records to sort: ")
        if (not NUM_REGEX.fullmatch(numOfRecords)):
            print("Invalid input")
            continue
        else:
            numOfRecords = int(numOfRecords)
            break

    # randomised array of records case
    print()
    HEADER_ONE = "-" * 15 + " RANDOMISED ARRAY " + "-" * 15
    print(HEADER_ONE)
    arr = [random.randint(0, 100000) for _ in range(numOfRecords)]

    # test the introsort algorithm (ascending order)
    print("\nSorting the array in ascending order...", end="")
    arrTestOne = arr.copy()
    timeTaken = timeit.timeit("intro_sort(arrTestOne, reverse=False)", setup="from __main__ import intro_sort, arrTestOne", number=1)
    print(f"\rSorted the array in {timeTaken} seconds in ascending order.")

    # test the correctness of the algorithm (ascending order)
    print("Testing the correctness of the algorithm...", end="")
    print(f"\rTest case verdict: {'X✓'[check_if_sorted(arrTestOne, modelArr=arr.copy())]}\033[K\n")
    del arrTestOne

    # test the introsort algorithm (descending order)
    print("\nSorting the array in descending order...", end="")
    arrTestTwo = arr.copy()
    timeTaken = timeit.timeit("intro_sort(arrTestTwo, reverse=True)", setup="from __main__ import intro_sort, arrTestTwo", number=1)
    print(f"\rSorted the array in {timeTaken} seconds in descending order.")

    # test the correctness of the algorithm (descending order)
    print("Testing the correctness of the algorithm...", end="")
    print(f"\rTest case verdict: {'X✓'[check_if_sorted(arrTestTwo, reverse=True, modelArr=arr.copy())]}\033[K\n")
    del arrTestTwo

    print("\nEnd of Tests!")
    print("-" * len(HEADER_ONE), end="\n\n")

    # Nearly sorted arrays
    arr = get_nearly_sorted_array(numOfRecords)
    HEADER_TWO = "-" * 13 + " NEARLY SORTED ARRAYS " + "-" * 13
    print(HEADER_TWO)

    # test the introsort algorithm (ascending order)
    print("\nSorting the array in ascending order...", end="")
    arrTestThree = arr.copy()
    timeTaken = timeit.timeit("intro_sort(arrTestThree, reverse=False)", setup="from __main__ import intro_sort, arrTestThree", number=1)
    print(f"\rSorted the array in {timeTaken} seconds in ascending order.")

    # test the correctness of the algorithm (ascending order)
    print("Testing the correctness of the algorithm...", end="")
    print(f"\rTest case verdict: {'X✓'[check_if_sorted(arrTestThree, modelArr=arr.copy())]}\033[K\n")
    del arrTestThree

    # test the introsort algorithm (descending order)
    print("\nSorting the array in descending order...", end="")
    arrTestFour = arr.copy()
    timeTaken = timeit.timeit("intro_sort(arrTestFour, reverse=True)", setup="from __main__ import intro_sort, arrTestFour", number=1)
    print(f"\rSorted the array in {timeTaken} seconds in descending order.")

    # test the correctness of the algorithm (descending order)
    print("Testing the correctness of the algorithm...", end="")
    print(f"\rTest case verdict: {'X✓'[check_if_sorted(arrTestFour, reverse=True, modelArr=arr.copy())]}\033[K\n")
    del arrTestFour

    print("\nEnd of Tests!")
    print("-" * len(HEADER_TWO))