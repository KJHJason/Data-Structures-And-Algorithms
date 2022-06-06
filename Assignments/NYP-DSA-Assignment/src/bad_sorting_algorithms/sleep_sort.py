# import standard libraries
from time import sleep
from threading import Timer

def add_to_list(el, arr:list) -> None:
    """
    Adds the element to the list.
    
    Used for sleepsort.
    
    Requires two arguments: 
    - el: the element to be added
    - arr: the list to be added to
    """
    arr.append(el)

def sleep_sort(arr:list, reverse:bool=False) -> list:
    """
    Creates different threads for each elements and 
    each thread sleeps for an amount of time proportional to the element's value.
    
    Sorts by pax number.
    
    Best Time Complexity: O(max(arr))
    Worst Time Complexity: O(max(arr))
    Average Time Complexity: O(max(arr))
    
    Space Complexity: O(n)
    
    Requires two arguments:
    - arr: the array to be sorted
    - reverse: if True, the array will be sorted in a descending order (default: False)
    
    Returns the new sorted array.
    
    References:
    - Sleep Sort ( Craziest Sorting Algorithm ) in 1 Minute with Visualisation & Code 
        - https://www.youtube.com/watch?v=Cp9mdJmVtvo&feature=youtu.be
    """
    newArr = []

    maxEl = arr[0] # initialise the first element to be the maximum element
    for el in arr:
        # if the current element is greater than the maximum element
        if (maxEl.get_pax_num() < el.get_pax_num()): 
            # set the current element as the maximum element
            maxEl = el

        # create a thread for each element with the interval proportional to the element's value
        # and add the element to the list by calling the add_to_list function
        Timer(el.get_pax_num(), add_to_list, (el, newArr)).start()

    # wait for all threads to finish
    sleep(maxEl.get_pax_num() + 1)
    if (not reverse):
        # return sorted array (in ascending order)
        return newArr

    # treat the array like a stack using .pop() to reverse it and return a new list
    # instead of using python's in-built .reverse() or [::-1]
    return [newArr.pop() for _ in range(len(newArr))]