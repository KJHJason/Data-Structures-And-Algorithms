def selection_sort(arr:list, reverse:bool=False) -> None:
    """
    Do a selection sort by package name
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package name
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
                if (arr[j].get_package_name() > arr[index].get_package_name()):
                    index = j
            else:
                # find the next smallest element to compare with index
                if (arr[j].get_package_name() < arr[index].get_package_name()):
                    index = j

        if (index != i):
            # swap the found minimum/maximum element with the element at index i if the smallest/biggest 
            # elemment is not in its proper position
            arr[i], arr[index] = arr[index], arr[i]