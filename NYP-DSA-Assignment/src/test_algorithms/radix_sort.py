def counting_sort_for_radix_sort(arr:list[int], place:int, reverse:bool=False) -> None:
    """
    Counting sort for radix sort.
    
    Requires 3 arguments:
    - arr (list): The array of elements to sort by integer
    - place (int): The current digit number
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n+b)
    Worst time complexity: O(n+b)
    Average time complexity: O(n+b)
    
    Space complexity: O(n+b)
    Where n is the number of elements and b is the base number, 10
    """
    n = len(arr)
    outputArr = [0] * n
    countArr = [0] * 10

    # Calculate the number of occurrences of each digit
    for i in range(n):
        index = arr[i] // place
        countArr[index % 10] += 1

    # Calculate cumulative count...
    if (reverse):
        # in a descending order
        for i in range(8, -1, -1):
            countArr[i] += countArr[i + 1]
    else:
        # in an ascending order
        for i in range(1, 10):
            countArr[i] += countArr[i - 1]

    for i in range(n-1, -1, -1):
        # finding the index of the element in the count array by calculating the cost divided by the 
        # place value modulo 10 to get the remainder as to avoid index out of range error
        countArrIdx = (arr[i] // place) % 10

        # we will retrieve the element from the countArr using the countArrIdx we calculated above.
        # the retrieved element minus one (to account for indexing) will be the index of the element 
        # in the output array
        outputArr[countArr[countArrIdx] - 1] = arr[i]

        # decrement the count array by 1 for the next element
        countArr[countArrIdx] -= 1

    # Copy the sorted elements into original array
    for i in range(n):
        arr[i] = outputArr[i]

def radix_sort(arr:list, reverse:bool=False) -> None:
    """
    Do a radix sort (base 10) on the database by integer.
    
    Radix sort is a type of non-comparison sort which is different from most sorting algorithms 
    and uses the counting sort algorithm but solves the issue of 
    counting sort’s space complexity of O(n+k) where k is the largest number in the array 
    to O(n+b) where b is the base number 10.
    
    Its time complexity is linear in nature which can be significantly faster than other sorting
    algorithms for larger arrays, but it is also slower for smaller arrays.
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by integer
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(d(n+b))
    Worst time complexity: O(d(n+b))
    Average time complexity: O(d(n+b))
    where d is the number of digits in the largest number
    and b is the base number, 10. 
    
    References:
    - Radix Sort Algorithm Introduction in 5 Minutes
        - https://www.youtube.com/watch?v=XiuSW_mEn7g&feature=youtu.be
    """
    # Find the maximum number to know number of digits
    maxEl = max(arr)

    # Do counting sort for every digit based on palce value
    place = 1
    while (maxEl // place > 0):
        counting_sort_for_radix_sort(arr, place, reverse=reverse)
        place *= 10