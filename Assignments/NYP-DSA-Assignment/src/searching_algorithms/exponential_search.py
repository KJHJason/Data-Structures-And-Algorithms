from .binary_search import binary_search_for_name
from .search_utility_functions import find_all_name_occurrences

def exponential_search_for_customer(arr:list, target:str, descendingOrder:bool=False) -> tuple:
    """
    Do an exponential search on the database for customer name.
    
    Advantages over binary search:
    - If the element to be found is at the front of the array, it will be faster than binary search.
    
    Requires 2 arguments:
    - arr (list): The array of elements to search
    - target (int/float): The target to search for
    - descendingOrder (bool): Indicates the order of the array (True if descending order, defaults to False)
    
    Best time complexity: O(log(n))
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))
    
    References:
    - Exponential Search - better than Binary search? (Explained)
        - https://www.youtube.com/watch?v=BDVYtuWXgXE&feature=youtu.be
    """
    # if the array is empty
    if (len(arr) == 0):
        return -1, -1

    # if the target is the first element of the array
    if (arr[0] == target):
        return find_all_name_occurrences(arr, 0, target, "customerName") 

    # find the range of the target for the binary search
    # e.g. arr=[1, 2, 3, 4, 5, 6], target=3
    # first iteration: i = 1*2 = 2
    # second iteration: i = 2*2 = 4, since arr[4] = 5 which is larger than target
    # hence the while loop will break, and the range will be [left = 4//2 = 2, right=4]
    # which will be passed to the binary search function
    i = 1
    if (not descendingOrder):
        while (i < len(arr) and arr[i].get_customer_name() <= target):
            i *= 2
    else:
        while (i < len(arr) and arr[i].get_customer_name() >= target):
            i *= 2

    # if the range is found, do a binary search on the subarray
    return binary_search_for_name(arr, target, descendingOrder, "customerName", l=i//2, r=min(i, len(arr)-1))