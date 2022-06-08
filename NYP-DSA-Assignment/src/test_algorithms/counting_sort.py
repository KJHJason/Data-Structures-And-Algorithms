"""
Not implemented for the assignment since I already had radix sort which uses counting sort
but optimises its space complexity.
"""

def get_min_max(arr:list[int]) -> tuple[int, int]:
    """
    Returns the minimum and maximum values in the array
    
    Args:
        arr: list[int]
    """
    min_val = max_val = arr[0]

    for i in range(1, len(arr)):
        if (arr[i] < min_val):
            min_val = arr[i]
        if (arr[i] > max_val):
            max_val = arr[i]

    return min_val, max_val

def counting_sort(array:list[int], reverse:bool=False) -> None:
    """
    The counting sort algorithm sorts an array by counting 
    the number of occurrences of each element.
    It is a linear time algorithm in the worst case.
    
    Best time complexity: O(n+k) 
    Worst time complexity: O(n+k) 
    Average time complexity: O(n+k) 

    Space complexity: O(n+k) 
    where k is the range
    """
    n = len(array)

    minRange, maxRange = get_min_max(array)
    countRange = maxRange - minRange + 1

    outputArr = [0] * n

    # Initialize count array
    countArr = [0] * countRange

    # Store the count of each elements in count array
    for i in range(0, n):
        countArr[array[i] - minRange] += 1

    # Store the cummulative count
    if (not reverse):
        for i in range(1, countRange):
            countArr[i] += countArr[i - 1]
    else:
        for i in range(countRange - 2, -1, -1):
            countArr[i] += countArr[i + 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    for i in range(n - 1, -1, -1):
        outputArr[countArr[array[i] - minRange] - 1] = array[i]
        countArr[array[i] - minRange] -= 1

    # Copy the sorted elements into original array
    for i in range(0, n):
        array[i] = outputArr[i]