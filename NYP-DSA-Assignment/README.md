<h1 align="center">
    <img src="res/nanyang_polytechnic_logo.png" style="width: 50%; height: auto;" alt="NYP logo">
    <br>
    NYP Data Structures & Algorithms Assignment
</h1>

This assignment (40%) provided me the chance to implement the data structures and algorithms I've learnt in class and also through my own research to implement algorithms and data structures not taught in the module.

## Minimum Requirements
1. Design a suitable data structure (e.g. by making use of Python list, dictionary, objects, etc.) to manage the staycation booking records. 
    - You are required to store the following staycation booking records. 
    - Each record has: Package Name, Customer Name, number of pax and Package Cost per pax.

2. The data structure will store up to 10 records. 
    - All records are to be pre-initialized in the program.

3. Design a menu for the application to allow the user to perform the following:
    - Display all records
    - Sort record by Customer Name using Bubble sort
    - Sort record by Package Name using Selection sort
    - Sort record by Package Cost using Insertion sort
    - Search record by Customer Name using Linear Search and update record
    - Search record by Package Name using Binary Search and update record
    - List records range from $X to $Y. e.g $100-200
    - Exit Application

4. All sorting algorithms are in ascending order only. 
    - After sorting, the record will be stored as sorted order for next display.

5. All search algorithms MUST ignore case sensitivity. 
    - Upon update, the updated record will be stored.

6. Error handling is required.

7. User friendly interface and design

---

### Additional Data Structures & Algorithms Implemented

- Efficient Sorting Algorithms
    - Introsort ([intro_sort.py](src/sorting_algorithms/intro_sort.py))
    - Heap sort ([heap_sort.py](src/sorting_algorithms/heap_sort.py))
    - Tree sort ([AVLTree.py](src/data_structures/AVLTree.py))
    - Radix sort ([radix_sort.py](src/sorting_algorithms/radix_sort.py))
    - Shell sort ([shellsort.py](src/sorting_algorithms/shellsort.py))

- Search Algorithms
    - Fibonacci search ([fibonacci_search.py](src/searching_algorithms/fibonacci_search.py))
    - Exponential Search ([exponential_search.py](src/searching_algorithms/exponential_search.py))

- Data Structures
    - AVL Tree ([AVLTree.py](src/data_structures/AVLTree.py))
    - Doubly Linked List ([DoublyLinkedList.py](src/data_structures/DoublyLinkedList.py))

- Bad Sorting Algorithms
    - Bogosort ([bogo_sort.py](src/bad_sorting_algorithms/bogo_sort.py))
    - Bozosort ([bogo_sort.py](src/bad_sorting_algorithms/bogo_sort.py))
    - Gnome sort ([gnome_sort.py](src/bad_sorting_algorithms/gnome_sort.py))
    - Pancake sort ([pancake_sort.py](src/bad_sorting_algorithms/pancake_sort.py))
    - Sleep sort ([sleep_sort.py](src/bad_sorting_algorithms/sleep_sort.py))
    - Slow sort ([slow_sort.py](src/bad_sorting_algorithms/slow_sort.py))
    - Stalin sort ([stalin_sort.py](src/bad_sorting_algorithms/stalin_sort.py))