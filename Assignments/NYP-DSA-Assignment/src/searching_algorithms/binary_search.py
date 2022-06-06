from .search_utility_functions import find_all_name_occurrences, cost_upper_index, cost_lower_index

"""---------------------- BINARY SEARCH FOR PACKAGE NAME ----------------------"""

def binary_search_for_name(arr:list, target:str, descendingOrder:bool, typeOfSearch:str, l:int=None, r:int=None) -> tuple:
    """
    Do a binary search on the database for the package name
    
    Requires 3 argument:
    - arr (list): The array of elements to search
    - target (string)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    - typeOfSearch (str): indicates what to search by (customerName or packageName)
    
    2 Optional arguments:
    - l (int): left index (defaults to 0)
    - r (int): right index (defaults to n-1)
    
    Best time complexity: O(1)
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))
    """
    if (l is None and r is None):
        l = 0
        r = len(arr) - 1

    while (l <= r):
        mid = (l + r) // 2

        # return mid if the package name is found in the subarray
        if (arr[mid].get_val(typeOfSearch) == target):
            # will return the index of the first and last occurrence of the package name in a tuple
            return find_all_name_occurrences(arr, mid, target, typeOfSearch) 

        if (not descendingOrder):
            # if the package name to find is greater than mid, search the right half
            if (arr[mid].get_val(typeOfSearch) < target):
                l = mid + 1
            # if the package name to find is smaller than mid, search the left half
            else:
                r = mid - 1
        else:
            # if the package name to find is smaller than mid, search the right half
            if (arr[mid].get_val(typeOfSearch) > target):
                l = mid + 1
            # if the package name to find is greater than mid, search the left half
            else:
                r = mid - 1

    return -1, -1 # return -1 if the package name is not found

"""---------------------- END OF BINARY SEARCH FOR PACKAGE NAME ----------------------"""

"""---------------------- BINARY SEARCH FOR PACKAGE COST PER PAX ----------------------"""

def binary_search_for_range_of_cost(arr:list, lowRange:float, highRange:float, descendingOrder:bool) -> tuple:
    """
    Do a binary search on the database for the package name
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - lowRange (float)
    - highRange (float)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(1)
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))
    """
    l = 0
    r = len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2

        # return mid if the range is found in the subarray
        if (arr[mid].get_cost_per_pax() >= lowRange and arr[mid].get_cost_per_pax() <= highRange):
            if (descendingOrder):
                return cost_upper_index(arr, mid, highRange, descendingOrder),\
                    cost_lower_index(arr, mid, lowRange, descendingOrder)
            else:
                return cost_lower_index(arr, mid, lowRange, descendingOrder), \
                    cost_upper_index(arr, mid, highRange, descendingOrder)

        # decide which side of the sub-array to search based on the lower range
        if (not descendingOrder):
            # if the lower range to find is greater than mid, search the right half
            if (arr[mid].get_cost_per_pax() < lowRange):
                l = mid + 1
            # if the lower range to find is less than mid, search the left half
            else: # arr[mid].get_cost_per_pax() > lowRange
                r = mid - 1
        else:
            # if the lower range to find is greater than mid, search the right half
            if (arr[mid].get_cost_per_pax() > lowRange):
                l = mid + 1
            # if the lower range to find is less than mid, search the left half
            else: # arr[mid].get_cost_per_pax() < lowRange
                r = mid - 1

    return -1, -1 # return -1 if the package name is not found

"""---------------------- END OF BINARY SEARCH FOR PACKAGE COST PER PAX ----------------------"""