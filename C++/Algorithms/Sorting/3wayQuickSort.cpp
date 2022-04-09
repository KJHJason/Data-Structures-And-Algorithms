#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

void partition(vi& arr, int l, int r, int& i, int& j)
{
    /* 
    This function partitions the array into three parts:
    * a[l..i] contains all elements smaller than pivot
    * a[i+1..j-1] contains all occurrences of pivot
    * a[j..r] contains all elements greater than pivot 
    */

    i = l - 1, j = r;
    int p = l - 1, q = r, v = arr[r];

    while (true) {
        // From the left, find the first element greater than or equal to v. 
        // This loop will definitely terminate as v is last element
        while (arr[++i] < v);

        // From the right, find the first element smaller than or equal to v
        while (v < arr[--j]) {
            if (j == l) break;
        }

        // If i and j pointers intersects, then we are done and break out of the loop
        if (i >= j) break;

        // Swap so that smaller goes on left greater goes on the right
        std::swap(arr[i], arr[j]);

        // Move all same left occurrence of pivot to the beginning of array and keep count using p
        if (arr[i] == v) {
            p++;
            std::swap(arr[p], arr[i]);
        }

        // Move all same right occurrence of pivot to end of the array and keep count using q
        if (arr[j] == v) {
            q--;
            std::swap(arr[j], arr[q]);
        }
    }

    // Move pivot element to its correct index
    std::swap(arr[i], arr[r]);

    // Move all left same occurrences from beginning to adjacent to arr[i]
    j = i - 1;
    for (int k = l; k < p; k++, j--) std::swap(arr[k], arr[j]);

    // Move all right same occurrences from end to adjacent to arr[i]
    i = i + 1;
    for (int k = r - 1; k > q; k--, i++) std::swap(arr[i], arr[k]);
}

void quickSort(vi& arr, int l, int r)
{
    /*
    * Stable quick sort details:
    This quick sort algorithm sorts an array by taking an element as a pivot and dividing the array 
    into three parts, the elements less than the pivot, the elements equal to the pivot, and the 
    elements greater than the pivot.
    This algorithm is not stable and has a slightly higher overhead compared to the typical quick sort.

    * Best time complexity: O(n log n)
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n log n)
    
    * Space complexity: O(1) for this program though it will be O(log n) without pointers.
    
    * How it works: 
    * 1. Pick a pivot element from the array.
    * 2. Partition the array around the pivot.
    * 3. Recursively sort the sub-array on the left of the pivot and the sub-array on the right of the pivot.
    */
    if (l >= r) return; 

    int i{}, j{};

    // partition the array
    partition(arr, l, r, i, j);

    // sorting the left part
    quickSort(arr, l, j);

    // sorting the right part
    quickSort(arr, i, r);
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