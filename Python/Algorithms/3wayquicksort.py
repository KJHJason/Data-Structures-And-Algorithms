def partition(arr, low, high, reverse):
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

    # initialise mid pointer and pivot
    mid = low
    pivot = arr[high]
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


def three_way_quicksort(arr, low, high, reverse=0):
    """
    3-way quicksort algorithm for sorting an array in ascending or descending order
    
    Main idea is to partition the array into three parts using the "Dutch National Flag Algorithm".
    
    Advantages of 3way quicksort over the traditional quicksort algorithm is that it is able to sort the array quicker if there are many duplicate values.
    
    Time Complexities:
    - Best case: O(n(log(n)))
    - Worst case: O(n^2)
    - Average case: O(n(log(n)))
    
    Space Complexity:
    - O(1) in this function
    
    Args:
    - arr (list): The array to be sorted
    - low (int): The lower index of the array
    - high (int): The higher index of the array
    - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
    """
    if (low >= high): 
        return

    # partition the array
    i, j = partition(arr, low, high, reverse)

    # sort the left half recursively
    three_way_quicksort(arr, low, i, reverse)
    
    # sort the right half recursively
    three_way_quicksort(arr, j, high, reverse)

if (__name__ == "__main__"):
    # test codes
    arr = [10, 1, 2, 3, 1, 2, 5, 1000000, 1000 ,-1000, -12903, 2, 3455, 2324]
    three_way_quicksort(arr, 0, len(arr) - 1)
    print(arr)

    three_way_quicksort(arr, 0, len(arr) - 1, 1)
    print(arr)