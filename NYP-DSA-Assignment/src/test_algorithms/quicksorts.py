"""
Not implemented for the assignment since this algorithm is taught in the module.
Hence, there was no extra marks for implementing this algorithm in the assignment.
"""

def median_of_3(arr:list[int], firstIndex:int, middleIndex:int, lastIndex:int) -> int:
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
    if ((arr[firstIndex] > arr[middleIndex]) ^ (arr[firstIndex]> arr[lastIndex])):
        return arr[firstIndex]

    if ((arr[middleIndex] > arr[firstIndex]) ^ (arr[middleIndex] > arr[lastIndex])):
        return arr[middleIndex]

    return arr[lastIndex]

"""--------------------------- 3 WAY QUICKSORT ---------------------------"""

def partition_to_3(arr:list[int], low:int, high:int, pivot:int, reverse:bool=False) -> tuple:
    """
    Partition the array into three parts:

    In an ascending order,
    - arr[low...i] contains all the elements smaller than the pivot
    - arr[i+1...j-1] contains all the elements equal to the pivot
    - arr[j...high] contains all the elements larger than the pivot

    In a descending order,
    - arr[low...i] contains all the elements larger than the pivot
    - arr[i+1...j-1] contains all the elements equal to the pivot
    - arr[j...high] contains all the elements smaller than the pivot
    
    Args:
    - arr (list): The array to be sorted
    - low (int): The lower index of the array
    - high (int): The higher index of the array
    - reverse (bool): Whether the array is sorted in ascending or descending order.
    """
    # if looking at two or less elements
    if (high - low <= 1):
        # swap the elements if in wrong order
        if (not reverse):
            if (arr[high] < arr[low]):
                arr[high], arr[low] = arr[low], arr[high]
        else:
            if (arr[high] > arr[low]):
                arr[high], arr[low] = arr[low], arr[high]

        return low, high # i, j pointers for the next recursive call

    # initialise mid pointer
    mid = low
    while (mid <= high):
        # if the element is smaller than the pivot, swap it the elements
        if (arr[mid] < pivot):
            if (not reverse):
                # Ascending order: swap the elements with the high pointer such that the smaller element is on the left
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            else:
                # Descending order: swap the elements with the low pointer such that the smaller element is on the right
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        # if there are values that are the same as the pivot
        elif (arr[mid] == pivot):
            # increment the mid pointer to move to the next element
            mid += 1

        # if the element is greater than the pivot, swap it with the element at the high pointer
        elif (arr[mid] > pivot):
            if (not reverse):
                # Ascending order: swap the elements with the low pointer such that the larger element is on the right
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            else:
                # Descending order: swap the elements with the high pointer such that the larger element is on the left
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1

    return low - 1, mid # i, j pointers for the next recursive call

def _three_way_quicksort(arr:list[int], low:int, high:int, reverse:bool=False) -> None:
    """
    3-way quicksort algorithm for sorting an array in ascending or descending order
    
    Main idea is to partition the array into three parts using the "Dutch National Flag Algorithm".
    
    Advantages of 3way quicksort over the traditional quicksort algorithm is 
    that it is able to sort the array quicker if there are many duplicate values.
    
    Time Complexities:
    - Best case: O(n log n)
    - Worst case: O(n^2)
    - Average case: O(n log n)
    
    Space Complexity:
    - O(1) as it sorts in place
    
    Args:
    - arr (list): The array to be sorted
    - low (int): The lower index of the array
    - high (int): The higher index of the array
    - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
    """
    if (low >= high): 
        return

    # partition the array
    pivot = median_of_3(arr, low, (low + high) // 2, high)
    i, j = partition_to_3(arr, low, high, pivot, reverse=reverse)

    # sort the left half recursively
    _three_way_quicksort(arr, low, i, reverse=reverse)

    # sort the right half recursively
    _three_way_quicksort(arr, j, high, reverse=reverse)

def three_way_quicksort(arr:list[int], reverse:bool=False) -> None:
    """
    Helper function for the 3-way quicksort algorithm
    
    Args:
    - arr (list): The array to be sorted
    - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
    """
    _three_way_quicksort(arr, 0, len(arr) - 1, reverse=reverse)

"""--------------------------- END OF 3 WAY QUICKSORT ---------------------------"""

"""--------------------------- QUICKSORT ---------------------------"""

def partition_to_2(arr:list[int], low:int, high:int, pivot:int, reverse:bool=False) -> int:
    """
    Unlike the 3-way quicksort, the 2-way quicksort does not partition the array into three parts.
    
    Instead, it partitions the array into two parts:
    - arr[low...i] contains all the elements smaller than the pivot
    - arr[i+1...high] contains all the elements larger than the pivot
    """
    i = low
    j = high - 1
    while (1):
        if (not reverse):
            # find the first element in the array which is smaller than the pivot
            while (arr[i] < pivot):
                i += 1

            # find the first element in the array which is larger than the pivot
            while (arr[j] > pivot):
                j -= 1
        else:
            # find the first element in the array which is larger than the pivot
            while (arr[i] > pivot):
                i += 1

            # find the first element in the array which is smaller than the pivot
            while (arr[j] < pivot):
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

def _quicksort(arr:list[int], start:int, end:int, reverse:bool=False) -> None:
    """
    The quick sort algorithm sorts an array by taking an element as a pivot and 
    dividing the array into two parts, one with elements less than the pivot and 
    the other with elements greater than the pivot.
    
    Time Complexities:
    - Best case: O(n log n)
    - Worst case: O(n^2)
    - Average case: O(n log n)
    
    Space Complexity:
    - O(log n) for the call stack
    
    Args:
    - arr (list): The array to be sorted
    - start (int): The lower index of the array
    - end (int): The length of the array/highest index + 1
    - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
    """
    while (end - start > 1):
        # get the pivot for quick sort using the median of three concept
        pivot = median_of_3(arr, start, start + ((end - start) // 2), end - 1)

        # print("\rPivot:", pivot, "Start:", start, "End:", end, end="")

        # partition the array around the pivot
        partitionRes = partition_to_2(arr, start, end, pivot, reverse=reverse)

        # recursive case:
        # sort right half of the array recursively by changing the start pointer to the pivot
        _quicksort(arr, partitionRes, end, reverse=reverse)
        
        # change pointer of end to sort the left half of the array
        end = partitionRes

# def partition_to_2(arr:list[int], low:int, high:int, reverse:bool=False) -> int:
#     """
#     Unlike the 3-way quicksort, the 2-way quicksort does not partition the array into three parts.
    
#     Instead, it partitions the array into two parts:
#     - arr[low...i] contains all the elements smaller than the pivot
#     - arr[i+1...high] contains all the elements larger than the pivot
#     """
#     # choose the rightmost element as pivot
#     pivot = arr[high]

#     # pointer for greater element
#     i = low - 1

#     # traverse through all elements
#     # compare each element with pivot
#     for j in range(low, high):
#         if (not reverse and arr[j] <= pivot):
#             # if element smaller than pivot is found
#             # swap it with the greater element pointed by i
#             i += 1
#             # swapping element at i with element at j
#             arr[i], arr[j] = arr[j], arr[i]
#         elif (reverse and arr[j] >= pivot):
#             # if element larger than pivot is found
#             # swap it with the smaller element pointed by i
#             i += 1

#             # swapping element at i with element at j
#             arr[i], arr[j] = arr[j], arr[i]

#     # swap the pivot element with the greater element specified by i
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]

#     # return the position from where partition is done
#     return i + 1

# def _quicksort(arr:list[int], start:int, end:int, reverse:bool=False) -> None:
#     """
#     The quick sort algorithm sorts an array by taking an element as a pivot and 
#     dividing the array into two parts, one with elements less than the pivot and 
#     the other with elements greater than the pivot.
    
#     Time Complexities:
#     - Best case: O(n log n)
#     - Worst case: O(n^2)
#     - Average case: O(n log n)
    
#     Space Complexity:
#     - O(log n) for the call stack
    
#     Args:
#     - arr (list): The array to be sorted
#     - start (int): The lower index of the array
#     - end (int): The length of the array/highest index + 1
#     - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
#     """
#     if (start < end):
#         # partition the array
        
#         p = partition_to_2(arr, start, end, reverse=reverse)

#         # sort the left half recursively
#         _quicksort(arr, start, p - 1, reverse=reverse)

#         # sort the right half recursively
#         _quicksort(arr, p + 1, end, reverse=reverse)

def quicksort(arr:list[int], reverse:bool=False) -> None:
    """
    Helper function for the quick sort algorithm
    
    Args:
    - arr (list): The array to be sorted
    - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
    """
    _quicksort(arr, 0, len(arr), reverse=reverse)

"""--------------------------- END OF QUICKSORT ---------------------------"""