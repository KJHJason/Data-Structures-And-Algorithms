#include <iostream>
#include <string>
#include <vector>

typedef std::vector<int> vi;

int iterativeBinarySearch(const vi& arr, const int& elementToFind, int& l, int& r)
{
    /*
    * Iterative Binary Search Details:
    * This is a search algorithm that works by dividing the array into two parts, the left part and the right part.
    * The left part contains all the elements that are smaller than the element to be found.
    * The right part contains all the elements that are larger than the element to be found.
    * The algorithm then repeats the process until the element is found or the left part is empty.

    * Best time complexity: O(1)
    * Average time complexity: O(log n)
    * Worst time complexity: O(log n)
    * Space complexity: O(1)
    */
    while (l <= r) {
        int mid = l + (r - l) / 2;

        // Check if elementToFind is present at mid
        if (arr[mid] == elementToFind) return mid;

        // If elementToFind greater, ignore left half
        if (arr[mid] < elementToFind) l = mid + 1;

        // If elementToFind is smaller, ignore right half
        else r = mid - 1;
    }

    return -1; // return -1 if element is not present
}

/*
    * Recursive Binary Search Details:
    * Same as the iterative binary search algorithm, but this algorithm is recursive.
    * This is a search algorithm that works by dividing the array into two parts, the left part and the right part.
    * The left part contains all the elements that are smaller than the element to be found.
    * The right part contains all the elements that are larger than the element to be found.
    * The algorithm then repeats the process until the element is found or the left part is empty.
    * The algorithm is recursive because it calls itself.

    * Best time complexity: O(1)
    * Average time complexity: O(log n)
    * Worst time complexity: O(log n)
    * Space complexity: O(1)
*/
int recursiveBinarySearch(const vi& arr, const int& elementToFind, int l, int r)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;

        // If the element is present at the middle
        if (arr[mid] == elementToFind) return mid;

        // If element is smaller than mid, then it can only be present in left subarray
        if (arr[mid] > elementToFind) return recursiveBinarySearch(arr, elementToFind, l, mid - 1);

        // Else the element can only be present in right subarray
        return recursiveBinarySearch(arr, elementToFind, mid + 1, r);
    }

    return -1; // return -1 if element does not exist in array
}

int main()
{
    std::cout << "How many elements to generate?: ";
    int n; std::cin >> n;
    vi arr;
    for (int i = 0; i < n; i++) {
        arr.push_back(i);
    }
    int l = 0; 
    int r = arr.size() - 1; // -1 to account for indexing

    std::cout << "Elements has been generated (0 - " << n - 1 << ")...\n";

    std::cout << "\nEnter the element to search for: ";
    int x; std::cin >> x;

    if (iterativeBinarySearch(arr, x, l, r) != -1) {
        std::cout << "Element found: " << x << " via iterative binary search\n";
    } else {
        std::cout << "Element not found\n";
    }

    if (recursiveBinarySearch(arr, x, l ,r) != -1) {
        std::cout << "Element found: " << x << " via recursive binary search\n";
    } else {
        std::cout << "Element not found\n";
    }
    return 0;
}