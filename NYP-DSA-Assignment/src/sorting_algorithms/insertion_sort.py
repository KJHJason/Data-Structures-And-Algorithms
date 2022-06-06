def insertion_sort(arr:list, reverse:bool=False, startIdx:int=None, endIdx:int=None, mode:str="costPerPax") -> None:
    """
    Do a insertion sort by package cost per pax, package name, and more.
    However, this function is used in the program to sort by cost per pax and package name
    
    Requires 5 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order 
        - Default: False
    - startIdx (int): The index of the first element to sort
        - Default: 0
    - endIdx (int): The index to stop at when sorting (exclusive of endIdx, i.e. [...endIdx-1])
        - Default: len(arr)
    - mode (str): The mode of sorting. Can be "costPerPax" or "packageName", etc.
        - default: "costPerPax"
    
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
        el = arr[i] # save the element to be positioned

        # now find the position where el fits in the ordered part of the array
        j = i
        if (not reverse):
            # Compare el with each element on the left of it and
            # shift the bigger element to the right of their current position
            while (j > startIdx and el.get_val(mode) < arr[j-1].get_val(mode)):
                arr[j] = arr[j-1]
                j -= 1
        else:
            # Compare el with each element on the left of it and
            # shift the smaller element to the right of their current position
            while (j > startIdx and el.get_val(mode) > arr[j-1].get_val(mode)):
                arr[j] = arr[j-1]
                j -= 1

        # Put the saved element into the open slot
        arr[j] = el