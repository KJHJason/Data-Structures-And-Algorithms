"""
Functions in this python file is used for the introsort algorithm.

The functions here are basically functions for the quicksort algorithm to be used
in the introsort algorithm.
"""

def median_of_3(arr:list, firstIndex:int, middleIndex:int, lastIndex:int) -> str:
    """
    Find the median of three elements in the array (comparing the first, middle, and last elements).
    Helps to reduce the chance of picking a bad pivot to partition around which can make
    quicksort slow.
    
    Requires four arguments:
    - arr (list): the array to find the median of three elements in
    - firstIndex (int): the index of the first element in the array
    - middleIndex (int): the index of the middle element in the array
    - lastIndex (int): the index of the last element in the array
    
    Returns the element in the array which is the median of the three elements.
    """
    # if the first element is larger than the middle but smaller than the last element
    # or if the first element is smaller than the middle but larger than the last element
    # Note: using the bitwise XOR operator
    if ((arr[firstIndex].get_package_name() > arr[middleIndex].get_package_name()) ^ (arr[firstIndex].get_package_name() > arr[lastIndex].get_package_name())):
        return arr[firstIndex]

    # if the middle element is larger than the first element but smaller than the last element
    # or if the middle element is smaller than the last element but larger than the last element
    # Note: using the bitwise XOR operator
    if ((arr[middleIndex].get_package_name() > arr[firstIndex].get_package_name()) ^ (arr[middleIndex].get_package_name() > arr[lastIndex].get_package_name())):
        return arr[middleIndex]

    # if the last element is larger than the first element but smaller than the middle element
    # or if the last element is smaller than the first element but larger than the middle element
    return arr[lastIndex]

def partition(arr:list, l:int, r:int, pivot:str, reverse:bool=False) -> int:
    """
    Partition the array into two parts using the pivot:
    - The elements smaller than the pivot will be on the left of the pivot
    - The elements larger than the pivot will be on the right of the pivot
    
    Requires five arguments:
    - arr (list): the array to partition
    - l (int): the starting index of the array
    - r (int): the ending index of the array
    - pivot (str): the package name to partition the array around
    - reverse (bool): if True, the array will be sorted in a descending order (default: False)
    """
    i = l
    j = r - 1 # - 1 to avoid the index out of range error
    while (1):
        if (not reverse):
            # find the first element in the array which is smaller than the pivot
            while (arr[i].get_package_name() < pivot):
                i += 1

            # find the first element in the array which is larger than the pivot
            while (arr[j].get_package_name() > pivot):
                j -= 1
        else:
            # find the first element in the array which is larger than the pivot
            while (arr[i].get_package_name() > pivot):
                i += 1

            # find the first element in the array which is smaller than the pivot
            while (arr[j].get_package_name() < pivot):
                j -= 1

        # if the two pointers have crossed, return i
        if (i >= j):
            return i

        # swap the two elements that are not in the correct position
        # e.g. [1, 5, 3, 2, 4], pivot = 3 (element), i = 1, j = 3
        # swap 5 and 2 and the array becomes [1, 2, 3, 5, 4]
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1