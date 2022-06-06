def slow_sort(arr:list, i:int, j:int, reverse:bool=False) -> None:
    """
    Based on the principle of multiply and surrender which is the opposite of divide and conquer.
    
    Sorts by package cost.
    
    According to GeeksforGeeks, its time complexities are;
    Best Time Complexity: O(n^2.709)
    Worst Time Complexity: O(n^2.709)
    Average Time Complexity: O(n^2.709)
    which is worse than other O(n^2) algorithms such as bubble sort
    
    Works by 
    - Splitting the array into two halves
    - Sort each halves recursively, and then compare the highest element from each half
    - Move the highest element to the end of the array
    - Repeat the process from the top excluding the highest elements at the end for the remaining elements
    
    Requires four arguments:
    - arr: the array to be sorted
    - i: the starting index of the array
    - j: the ending index of the array
    - reverse: if True, the array will be sorted in a descending order (default: False)
    
    References:
    - Slow Sort Visualisation
        - https://youtu.be/QbRoyhGdjnA
    """
    # base case
    if (i >= j):
        return

    mid = (i + j) // 2

    # recursively sort the left half
    slow_sort(arr, i, mid, reverse=reverse)

    # recursively sort the right half
    slow_sort(arr, mid + 1, j, reverse=reverse)

    if (not reverse):
        # swap the elements if jth element is greater than the mid element
        if (arr[j].get_cost_per_pax() < arr[mid].get_cost_per_pax()):
            arr[j], arr[mid] = arr[mid], arr[j]
    else:
        # swap the elements if jth element is less than the mid element
        if (arr[j].get_cost_per_pax() > arr[mid].get_cost_per_pax()):
            arr[j], arr[mid] = arr[mid], arr[j]

    # recursively sort the whole array again except the last jth element as it is the maximum element
    slow_sort(arr, i, j - 1, reverse=reverse)