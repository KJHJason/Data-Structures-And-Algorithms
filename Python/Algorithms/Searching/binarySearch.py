def iterative_binary_search(arr, target):
    """
    Iterative binary search:
    - Find the midpoint of the array
    - If the midpoint is the target, return the midpoint
    - If the midpoint is greater than the target, search the left half of the array
    - If the midpoint is less than the target, search the right half of the array

    Time Complexities:
    - Best case: O(1)
    - Worst case:  O(n log n)
    - Average case: O(log n)
    
    Space Complexity:
    - O(1) in this function
    
    Args:
    - arr: the list to look through
    - target: the value to look for
    
    Returns:
    - the index of the target if found, -1 otherwise
    """
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    return -1

def recursive_binary_search(arr, target, low=0, high=0):
    """
    Recursive binary search:
    - Find the midpoint of the array
    - If the midpoint is the target, return the midpoint
    - If the midpoint is not the target, recursively call the function on the left or right half of the array
    - If the midpoint is greater than the target, search the left half of the array
    - If the midpoint is less than the target, search the right half of the array
    - Note: Since this algorithm is recursive, it is slower than the iterative version due to the overhead of the recursive calls.

    Time Complexities:
    - Best case: O(1)
    - Worst case:  O(n log n)
    - Average case: O(log n)
    
    Space Complexity:
    - O(1) in this function
    
    Args:
    - arr: the list to look through
    - target: the value to look for
    
    Returns:
    - the index of the target if found, -1 otherwise
    """
    if (low > high):
        return -1

    mid = (low + high) // 2
    if (arr[mid] == target):
        return mid
    elif (arr[mid] < target):
        return recursive_binary_search(arr, target, low=mid + 1, high=high)
    else:
        return recursive_binary_search(arr, target, low=low, high=mid - 1)

if __name__ == "__main__":
    arr = [10, 23, 25, 34, 36, 42, 63, 74, 87, 92, 99]

    print("List element:\n", arr, sep="", end="\n\n")
    target = int(input("Enter the target number: "))

    print("\nUsing iterative binary search:")
    found = iterative_binary_search(arr, target)
    if (found != -1):
        print("Found at index: ", found)
    else:
        print("Not found")

    print("\nUsing recursive binary search:")
    found = recursive_binary_search(arr, target, low=0, high=len(arr) - 1)
    if (found != -1):
        print("Found at index: ", found)
    else:
        print("Not found")
