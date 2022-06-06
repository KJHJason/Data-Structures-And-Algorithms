def bubble_sort(arr:list, reverse:bool=False) -> None:
    """
    Do a bubble sort (optimised ver) on the database by customer name
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by customer name
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)
    """
    for i in range(len(arr) - 1): # -1 to stop at last element since the last element will be the highest element after an iteration from the nested for loop
        swapFlag = 0
        for j in range(len(arr) - i - 1): # -i to stop at last i element since they are already sorted and -1 to account for the indexing starting from 0
            if (reverse):
                # swap the elements if the jth customer name is smaller than the next customer name
                if (arr[j].get_customer_name() < arr[j + 1].get_customer_name()):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapFlag = 1
            else:
                # swap the elements if the jth customer name is greater than the next customer name
                if (arr[j].get_customer_name() > arr[j + 1].get_customer_name()):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapFlag = 1

        if (not swapFlag):
            break # break when the array is already sorted