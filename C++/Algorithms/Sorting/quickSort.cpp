#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

int partition(vi& arr, int l, int r)
{
    int pivot = arr[r]; // set the pivot to the right of the partition
    int i = l - 1; // set the i pointer to l - 1 of the partition

    // iterate from index l to r - 1 (before the pivot)
    // This for loop will swap the element at index j with the 
    // element at index i where the element is smaller than the pivot
    for (int j = l; j < r; j++) {
        if (arr[j] < pivot) {
            i++; // increment i pointer in the partition
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[r]); // swap the element at index i + 1 with the pivot as we want the pivot to be between index i and j
    return i + 1; // return the new index of the pivot
}

void quickSort(vi& arr, int l, int r)
{
    /*
    * Quick sort details:
    The quick sort algorithm sorts an array by taking an element as a pivot and dividing the array into two parts, one with elements less than the pivot and the other with elements greater than the pivot.
    This algorithm is not stable.
    
    * Best time complexity: O(n log n)
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n log n)
    
    * Space complexity: O(1) for this program though it will be O(log n) without pointers.
    
    * How it works: 
    * 1. Take an element as a pivot and divide the array into two parts, one with elements less than the pivot and the other with elements greater than the pivot
    * 2. Recursively sort the two parts
    * 3. Merge the two sorted parts
    */
    if (l >= r) return; 

    // partition the array
    int p = partition(arr, l, r);
    
    // sorting the left part
    quickSort(arr, l, p - 1);

    // sorting the right part
    quickSort(arr, p + 1, r);
}

int main()
{
    vi arr;
    std::cout << "Enter number of elements: ";
    int n; std::cin >> n;
    std::cout << "\n";

    std::cout << "Enter elements (with spaces as the delimiter):\n";
    for (int i=0; i < n; i++) {
        int x; std::cin >> x;
        arr.push_back(x);
    }

    std::cout << "\nSorted elements:\n";
    quickSort(arr, 0, n - 1);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}