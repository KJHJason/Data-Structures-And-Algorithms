def stalin_sort(arr:list, reverse:bool=False) -> list:
    """
    ⡿⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠞⠛⠁⠄⡼⣿⣿⣿\n
    ⣿⡇⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⣦⠐⠠⡥⣿⣿\n
    ⣿⡇⠄⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⡔⠛⣿⣿\n
    ⣿⡇⢰⢏⣤⣦⣤⣍⣉⣿⣿⣿⡟⢋⣁⣤⣤⣤⣈⢻⣿⣿⣿⣿⠚⣯⡄⣿⣿\n
    ⣿⡇⣾⣿⣉⣀⣠⠅⠄⣽⣿⣿⣇⠈⢈⣉⣩⣐⡙⢿⣿⣿⣿⣿⠤⢿⢱⣿⣿\n
    ⣿⠁⣿⣿⣿⣿⣿⣦⣾⣿⣿⣿⣿⣷⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠾⣿⣿\n
    ⡏⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡇⣿⣿\n
    ⣧⢾⣿⣿⣿⣿⣿⣾⣯⣽⣋⠽⢭⣽⣤⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⠄⣿⣿⣿\n
    ⣿⣿⣿⣿⣿⣿⠿⠩⣭⣽⠁⢣⢿⣯⡉⣿⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⠿⠁⠄⠈⠋⠈⠄⡈⠁⠒⠌⠊⣃⠹⣿⣿⣿⣿⣿⣏⣻⣿⣿⣿⣿\n
    ⣿⣿⣿⣷⣶⣤⣤⣶⣿⣿⣿⡿⣿⣷⣤⣄⣤⣠⣼⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠸⣿⣿⣿⣿\n
    ⣿⣿⡿⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣷⣿⣿⣿⣿⣿\n
    ⡿⠛⠄⠄⠄⠙⢿⣷⣿⣭⣤⣬⡁⢉⣻⣿⣿⣿⣿⣿⣿⡟⠄⠹⣿⣿⣿⣿⣿\n
    
    This sorting algorithm is a popular joke/meme in the programming community as elements in the 
    array can be LOST/DELETED because it sorts the array by removing any elements that 
    are not in the correct order.
    
    Sorts by customer name.
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n)
    Average Time Complexity: O(n)
    
    Space Complexity: O(n)

    Requires two arguments:
    - arr: the array to be sorted
    - reverse: if True, the array will be sorted in a descending order (default: False)
    
    Returns the new sorted array.
    
    References:
    - Implementations of stalin sort
        - https://github.com/gustavo-depaula/stalin-sort
    """
    if (len(arr) <= 1):
        return arr

    temp = arr[0]
    newArr = []
    for el in arr:
        if (not reverse):
            if (el.get_customer_name() >= temp.get_customer_name()):
                newArr.append(el)
                temp = el
        else:
            if (el.get_customer_name() <= temp.get_customer_name()):
                newArr.append(el)
                temp = el

    return newArr