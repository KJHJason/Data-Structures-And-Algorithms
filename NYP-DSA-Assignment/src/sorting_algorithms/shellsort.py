def shellsort(arr:list, reverse:bool=False) -> None:
    """
    Shellsort algorithm works like the insertion sort algorithm but
    shellsort will sort the elements that are far apart from each other,
    and progressively reduces the interval gap between the elements to be compared.
    This effectively means that shellsort will do less shifting as compared to insertion sort.
    
    Sorts by pax number
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best Time Complexity: O(n log n)
    Average Time Complexity: O(n log n)
    Worst Time Complexity: O(n^2)
    Note: That the time complexity depends on the intervals used in the algorithm
    
    Reference:
    - Shell sort vs Insertion sort
        - https://youtu.be/g06hNBhoS1k
    - Explanation and Python implementation:
        - https://www.programiz.com/dsa/shell-sort
    """
    # initialise the gap by halving the array size first
    gap = len(arr) // 2

    while (gap > 0):
        # loop through the elements in the array in intervals of the gap
        for i in range(gap, len(arr)):
            temp = arr[i] # save the current element as temp

            # rearrange the elements at n/2, n/4, n/8,... intervals
            j = i
            if (not reverse):
                # if j is still greater or equal to the gap,
                # checks if the element at j-gap is greater than temp,
                # where j - gap is the element at the first element of the gap
                while (j >= gap and arr[j - gap].get_pax_num() > temp.get_pax_num()):
                    arr[j] = arr[j - gap] # if it is, shift the elements by replacing the 
                                          # element at j with the element at j-gap
                    j -= gap
            else:
                # same as the previous while loop, but checks if the element at j-gap is less than temp
                while (j >= gap and arr[j - gap].get_pax_num() < temp.get_pax_num()):
                    arr[j] = arr[j - gap]
                    j -= gap

            # finally, replace the value at j with temp at the open slot
            arr[j] = temp 

        gap //= 2 # halve the gap