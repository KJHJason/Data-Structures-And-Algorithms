def binary_search(arr:list[int], start:int, end:int, key:int, reverse:bool=False) -> int:
    """
    Do a binary search by integer.
    Args:
        arr (list): The array of elements to search
        start (int): The index of the first element to search
        end (int): The index to stop at when searching (exclusive of endIdx, i.e. [...endIdx-1])
        key (int): The key to search for
        reverse (bool): True if the list is to be searched in descending order
    
    Best time complexity: O(1)
    Worst time complexity: O(logn)
    Average time complexity: O(logn)
    """
    while (start <= end):
        mid = (start + end) >> 1 # floor division using bitwise operator, shift bits to the right by 1
        if (key == arr[mid]):
            return mid

        if (reverse):
            if (key < arr[mid]):
                start = mid + 1
            else:
                end = mid - 1
        else:
            if (key < arr[mid]):
                end = mid - 1
            else:
                start = mid + 1

    return start

def bin_insertion_sort(arr:list[int], reverse:bool=False, startIdx:int=None, endIdx:int=None) -> None:
    """
    Do a insertion sort by integer.
    However, this function is used in the program to sort by integer
    
    Requires 5 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order 
        - Default: False
    - startIdx (int): The index of the first element to sort
        - Default: 0
    - endIdx (int): The index to stop at when sorting (exclusive of endIdx, i.e. [...endIdx-1])
        - Default: len(arr)
    
    Best time complexity: O(n)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)
    """
    if (startIdx is None and endIdx is None):
        endIdx = len(arr)
        startIdx = 0

    if (startIdx == endIdx):
        # nothing to sort, hence just return 
        # if starting and ending index are the same
        return

    for i in range(startIdx+1, endIdx):
        el = arr[i] # save the element to be inserted

        # now find the position where el fits in the ordered part of the array
        pos = binary_search(arr, startIdx, i, el, reverse=reverse)

        # shift the elements to open up the slot for insertion
        for j in range(i, pos, -1):
            arr[j] = arr[j-1]

        # Put the saved element into the open slot
        arr[pos] = el