from .search_utility_functions import find_all_name_occurrences

def fibonacci_search_for_package_name(arr:list, target:str, descendingOrder:bool=False) -> tuple:
    """
    Fibonacci search algorithm works by using the Fibonacci numbers to
    determine the next index to check.
    Works by using the divide and conquer strategy to divide the array into unequal parts
    using the fibonacci sequence.
    
    Advantages over binary search:
    - More efficient on CPU where divisions are costly
        - However, nowadays CPUs are faster and the arithmetic performance differences 
        among division, addition, and subtraction are negligible.
        - Hence, it was widely used in the old days when computers were quite slow.
    
    Useful resources:   
    - Lecture 51A Fibonacci Search Data Structures Dec 01 2020 
        - https://youtu.be/K9n_mkLvRBs
    - https://iq.opengenus.org/fibonacci-search/
    - https://en.wikipedia.org/wiki/Fibonacci_search_technique
    - Explanation and Python implementation
        - https://www.codespeedy.com/fibonacci-search-algorithm-in-python/
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - target (string): The package name to search for
    - descendingOrder (bool): Indicates the order of the array (True if descending order, defaults to False)
    
    Best case: O(1) when the element to be found is the first element to be compared
    Worst case: O(log(n))
    Average case: O(log(n))
    """
    n = len(arr)
    fibMm2 = 0 # fib(m-2)
    fibMm1 = 1 # fib(m-1)
    fibM = fibMm2 + fibMm1 # fibM is the smallest fibonacci number greater than or equal to n
                           # calculated in the while loop below

    # Calculate fib(m) without using recursion
    while (fibM < n):
        fibMm2 = fibMm1
        fibMm1 = fibM
        fibM = fibMm2 + fibMm1

    offset = -1 # to use for discarding elements from front of the array for searching
    while (fibM > 1):
        i = min(offset + fibMm2, n - 1) # min() is used to avoid index out of range error
        if (arr[i].get_package_name() == target):
            return find_all_name_occurrences(arr, i, target, "packageName")

        if (not descendingOrder):
            # for ascending order
            if (arr[i].get_package_name() < target):
                # if the target is greater than the current element,
                # discard the first few elements from the front of the array by
                # moving the offset to the current index (offset + fib(m)-2) and lowering the fib(m) by one
                # as to search in the right side of the array
                fibM = fibMm1
                fibMm1 = fibMm2
                fibMm2 = fibM - fibMm1
                offset = i
            else: # if (arr[i] > target)
                # if the target is less than the current element,
                # lower the fibonacci term by two to search
                # in the left side of the array as to search in the left side of the array
                fibM = fibMm2
                fibMm1 -= fibMm2
                fibMm2 = fibM - fibMm1
        else:
            # for descendingOrder
            if (arr[i].get_package_name() > target):
                # if the target is less than the current element,
                # discard the first few elements from the front of the array by
                # moving the offset to the current index (offset + fib(m)-2) and lowering the fib(m) by one
                # as to search in the right side of the array
                fibM = fibMm1
                fibMm1 = fibMm2
                fibMm2 = fibM - fibMm1
                offset = i
            else: # if (arr[i] < target)
                # if the target is greater than the current element,
                # lower the fibonacci term by two to search
                # in the left side of the array as to search in the left side of the arrayw
                fibM = fibMm2
                fibMm1 = fibMm1 - fibMm2
                fibMm2 = fibM - fibMm1

    # to compare with the last element with the target
    # happens in instances such as when the target is the last element but fibn(m) is not > 1
    # e.g. arr = [1, 2, 3, 4, 5], target = 5,
    # before loop,    fibM = 5, fibMm1 = 3, fibMm2 = 2, offset = -1, i = undefined
    # after 1st loop, fibM = 3, fibMm1 = 2, fibMm2 = 1, offset = 1, i = 1
    # after 2nd loop, fibM = 2, fibMm1 = 1, fibMm2 = 1, offset = 2, i = 2
    # After 3rd loop, fibM = 1, fibMm1 = 1, fibMm2 = 0, offset = 3, i = 3 
    # Break out of loop since fibM is not more than 1, the loop stops 
    # and is unable to find the target in the last position
    # and thus the if statement below checks if the target is the last element
    if (fibMm1 and arr[n-1].get_package_name() == target):
        return find_all_name_occurrences(arr, n-1, target, "packageName")

    return -1, -1