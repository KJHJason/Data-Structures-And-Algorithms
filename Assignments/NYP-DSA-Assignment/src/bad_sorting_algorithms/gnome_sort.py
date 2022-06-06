def gnome_sort(arr:list, reverse:bool=False) -> None:
    """
    ⣿⣿⣿⣿⣿⠟⠉⠁⠄⠄⠄⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣏⠄⡠⡤⡤⡤⡤⡤⡤⡠⡤⡤⣸⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣗⢝⢮⢯⡺⣕⢡⡑⡕⡍⣘⢮⢿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⡧⣝⢮⡪⡪⡪⡎⡎⡮⡲⣱⣻⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⠟⠁⢸⡳⡽⣝⢝⢌⢣⢃⡯⣗⢿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⠟⠁⠄⠄⠄⠹⡽⣺⢽⢽⢵⣻⢮⢯⠟⠿⠿⢿⣿⣿⣿⣿⣿\n
    ⡟⢀⠄⠄⠄⠄⠄⠙⠽⠽⡽⣽⣺⢽⠝⠄⠄⢰⢸⢝⠽⣙⢝⢿\n
    ⡄⢸⢹⢸⢱⢘⠄⠄⠄⠄⠄⠈⠄⠄⠄⣀⠄⠄⣵⣧⣫⣶⣜⣾\n
    ⣧⣬⣺⠸⡒⠬⡨⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⣷⣽⣿⣿\n
    ⣿⣿⣿⣷⠡⠑⠂⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣄⠠⢀⢀⢀⡀⡀⠠⢀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣿⢐⢀⠂⢄⠇⠠⠈⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣧⠄⠠⠈⢈⡄⠄⢁⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣿⡀⠠⠐⣼⠇⠄⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣯⠄⠄⡀⠈⠂⣀⠄⢀⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    ⣿⣿⣿⣿⣿⣶⣄⣀⠐⢀⣸⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n
    
    Gnome sort, also known as stupid sort, is a sorting algorithm that works by 
    comparing the current element with the previous element and starts swapping elements 
    if they are not in order.
    
    E.g. arr = [3, 2, 1], sorting in ascending order...
    First iteration: [2, 3, 1], i = 0 (swap 2 and 3)
    Second iteration: [2, 3, 1], i = 2 (no swap)
    Third iteration: [2, 1, 3], i = 1 (swap 1 and 3)
    Fourth iteration: [1, 2, 3], i = 0 (swap 1 and 2)
    Fifth iteration: [1, 2, 3], i = 2 (no swap)
    Sixth iteration: [1, 2, 3], i = 3 (no swap and end loop)
    
    Similar to insertion sort but it is significantly slower than insertion as
    there is a lot of swappings involved.
    
    Useful resources:
    - GNOME SORT: How (NOT) To Sort Your Arrays.
        - https://youtu.be/pMjAllOR3eY
    
    Requires 2 arguments:
    - arr: the array to be sorted
    - reverse: if True, sorts in descending order (defaults to False)
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n^2)
    Average Time Complexity: O(n^2)
    """
    i = 0
    while (i < len(arr)):
        # if the current element is the first element, 
        # increment i to move to the next element
        if (i == 0):
            i += 1

        if (not reverse): 
            # ascending order
            if (arr[i - 1].get_pax_num() <= arr[i].get_pax_num()):
                # if the current element is greater than or equal to the previous element,
                # increment i to check the next element since it's in the correct order
                i += 1
            else:
                # if the current element is not in order, 
                # swap it with the previous element and decrement by 1
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        else: 
            # descending order
            if (arr[i - 1].get_pax_num() >= arr[i].get_pax_num()):
                # if the current element is smaller than or equal to the previous element,
                # increment i to check the next element since it's in the correct order
                i += 1
            else:
                # if the current element is not in order, 
                # swap it with the previous element and decrement by 1
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1