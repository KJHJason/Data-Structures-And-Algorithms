def flip(arr:list, i:int) -> None:
    """
    Flip the elements in the array (used to reverse arr[0..i])
    
    Requires 2 arguments:
    - arr (list): The array of elements to flip
    - i (int): The index of the element to flip
    """
    start = 0
    while (start < i):
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max_or_min(arr:list, n:int, reverse:bool=False, mode:str="packageName") -> int:
    """
    To find the index of the maximum or minimum element in arr[0..n-1]
    
    Requires four arguments:
    - arr (list): The array of elements to find the maximum or minimum element in
    - n (int): The size of the array
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    - mode (str): The mode of sorting (Default: "packageName")
    """
    if (not reverse):
        maxIdx = 0
        for i in range(0, n):
            if (arr[i].get_val(mode) > arr[maxIdx].get_val(mode)):
                maxIdx = i
        return maxIdx
    else:
        minIdx = 0
        for i in range(0, n):
            if (arr[i].get_val(mode) < arr[minIdx].get_val(mode)):
                minIdx = i
        return minIdx

def pancake_sort(arr:list, reverse:bool=False, mode:str="packageName") -> None:
    """
    Do a pancake sort on the database by package name.
    There will be O(n) number of flips performed to sort the array.
    In the worst case, there will be 2n-3 flips.

    Requires three arguments:
    - arr (list): The array of elements to sort by package name
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    - mode (str): The mode of sorting (Default: "packageName")
    
    Best time complexity: O(n) when the array is already sorted and no flips are needed.
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)
    
    Useful link for pancake sort visualisation:
    - Pancake sort algorithm, visualization with VTK
        - https://youtu.be/kk-_DDgoXfk
    """
    # start from n-1 and slowly reduce the size of the array
    for currSize in range(len(arr)-1, 0, -1):
        # get the index of the maximum or minimum value from the array based on the descending order argument
        # in arr[0..currSize+1]
        idxToFlip = find_max_or_min(arr, currSize + 1, reverse=reverse, mode=mode)
        if (idxToFlip != currSize):
            # flip the maximum or minimum value to index 0
            flip(arr, idxToFlip)

            # Now flip the maximum or minimum value to the sorted index
            flip(arr, currSize)