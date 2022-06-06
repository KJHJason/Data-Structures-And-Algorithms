from typing import Union

def linear_search_for_name(arr:list, target:str, typeOfSearch:str) -> Union[int, tuple]:
    """
    Do a linear search on the database for the customer name
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - target (string): The name to search for
    - typeOfSearch (string):"customerName" or "packageName"
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    
    Space complexity: O(n) for matched elements
    """
    if (typeOfSearch not in ("customerName", "packageName")):
        raise ValueError(f"Invalid search type, {typeOfSearch}, Must be either 'customerName' or 'packageName'!")

    matchedArr = []
    for i, record in enumerate(arr):
        if (record.get_val(typeOfSearch) == target):
            matchedArr.append((record, i))
    return -1 if (len(matchedArr) == 0) else matchedArr