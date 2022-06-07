"""
Not implemented for the assignment since this algorithm is taught in the module.
Hence, there was no extra marks for implementing this algorithm in the assignment.
"""

def merge_sort(arr:list[int], reverse:bool=False) -> None:
    """
    Sort the array using the merge sort algorithm.
    
    This is a sorting algorithm that works by dividing the array into two parts and 
    sorting them recursively (divide and conquer).
    The algorithm then merges the two sorted parts to form the final sorted array.
    
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n log n)
    
    Space complexity: O(n)
    
    Requires two arguments:
    - arr (list): The array to be sorted
    - reverse (bool): Whether the array is sorted in ascending or descending order. Defaults to False.
    """
    if (len(arr) > 1):
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge_sort(left, reverse=reverse)
        merge_sort(right, reverse=reverse)

        # i and j iterators for traversing the two halves
        # k iterators for the main array
        i = j = k = 0

        while (i < len(left) and j < len(right)):
            if (not reverse and left[i] <= right[j]):
                arr[k] = left[i]
                # Move the iterator forward
                i += 1
            elif (reverse and left[i] >= right[j]):
                arr[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            # Move to the next slot
            k += 1

        # place all the remaining values from the left half
        for i in range(i, len(left)):
            arr[k] = left[i]
            k += 1

        # place all the remaining values from the right half
        for j in range(j, len(right)):
            arr[k] = right[j]
            k += 1