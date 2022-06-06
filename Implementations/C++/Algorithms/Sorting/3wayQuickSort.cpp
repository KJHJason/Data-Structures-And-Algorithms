#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

/* 
    This function partitions the array into three parts:
    * a[l..i] contains all elements smaller than pivot
    * a[i+1..j-1] contains all occurrences of pivot
    * a[j..r] contains all elements greater than pivot
    --> Partition explanation credits: https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/
*/
void partition(vi& arr, int low, int high, int& i, int& j)
{
    // if there is two or less elements
    if (high - low <= 1) {
        // swap the elements if they are in the wrong order
        if (arr[high] < arr[low]) std::swap(arr[high], arr[low]); 
        i = low; j = high;
        return;
    }

    // initialise pointers
    int mid{low}, pivot{arr[high]};
    while (mid <= high) {
        // if the element is smaller than the pivot, swap it with the element
        // at the index pointed to the variable low then increment the low pointer
        if (arr[mid] < pivot) std::swap(arr[mid++], arr[low++]);
        // if the element is equal to the pivot, increment the mid pointer
        else if (arr[mid] == pivot) mid++;
        // if the element is bigger than the pivot, swap it with the element
        // at the index pointed to the variable high then decrement the high pointer
        else if (arr[mid] > pivot) std::swap(arr[mid], arr[high--]);
    }

    i = low - 1;
    j = mid;
}

/*
    * 3-way quick sort details:
    This quick sort algorithm sorts an array by taking an element as a pivot and dividing the array 
    into three parts, the elements less than the pivot, the elements equal to the pivot, and the 
    elements greater than the pivot.
    This algorithm uses the Dutch National Flag algorithm to partition the array.
    Additionally, this algorithm is not stable and has a slightly higher overhead compared to the typical 2-way quick sort.

    * Best time complexity: O(n log n)
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n log n)
    
    * Space complexity: O(1) for this program though it will be O(log n) without pointers.
    
    * How it works: 
    * 1. Pick a pivot element from the array.
    * 2. Partition the array around the pivot.
    * 3. Recursively sort the sub-array on the left of the pivot and the sub-array on the right of the pivot.
*/
void quickSort(vi& arr, int low, int high)
{
    if (low >= high) return; 

    int i{}, j{};

    // partition the array
    partition(arr, low, high, i, j);

    // sorting the left half recursively
    quickSort(arr, low, i);

    // sorting the right half recursively
    quickSort(arr, j, high);
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