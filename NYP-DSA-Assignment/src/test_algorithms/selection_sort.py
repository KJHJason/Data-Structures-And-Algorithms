def selection_sort(arr:list[int], reverse:bool=False) -> None:
    """
    Do a selection sort by integer
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by integer
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n^2)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)
    """
    dbSize = len(arr)
    for i in range(dbSize):
        # initialise the element at ith index and assume that it is 
        # the smallest/biggest element based on the reverse
        index = i

        for j in range(i + 1, dbSize):
            if (reverse):
                # find the next biggest element to compare with index
                if (arr[j] > arr[index]):
                    index = j
            else:
                # find the next smallest element to compare with index
                if (arr[j] < arr[index]):
                    index = j

        if (index != i):
            # swap the found minimum/maximum element with the element at index i if the smallest/biggest 
            # elemment is not in its proper position
            arr[i], arr[index] = arr[index], arr[i]