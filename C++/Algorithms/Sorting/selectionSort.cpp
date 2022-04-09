#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

void printVector(vi& arr)
{
    for (const auto& i : arr) std::cout << i << " ";
    std::cout << "\n";
}

void selectionSort(vi& arr, int n)
{
    /*
    * Selection Sort Details:
    * This is a sorting algorithm that works by selecting the smallest element from the unsorted part and putting it at the beginning.
    * The algorithm then repeats the process for the unsorted part.
    * This algorithm function is not stable.
    
    * Best time complexity: O(n^2)
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n^2)
    
    * Space complexity: O(1)

    * How it works:
    * 1. The algorithm starts by selecting the first element as the smallest element
    * 2.Then it selects the second element as the smallest element and compares it with the first element
    * 3. If the second element is smaller, then it is selected as the smallest element
    * 4. Then it compares the third element with the second element and so on
    * 5. The algorithm then repeats the process for the unsorted part
    */
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        std::swap(arr[i], arr[minIndex]);
    }
}

void stableSelectionSort(vi& arr, int n)
{
    /*
    * Stable Selection Sort Details:
    * This is a sorting algorithm that works by selecting the smallest element from the unsorted part and putting it at the beginning.
    * The algorithm then repeats the process for the unsorted part.
    * This algorithm function is stable.
    
    * Best time complexity: O(n^2)
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n^2)
    
    * Space complexity: O(1)

    * How it works:
    * 1. The algorithm starts by selecting the first element as the smallest element
    * 2. Find the minimum element in the unsorted array
    * 3. Move the minimum element to the current i in the iteration
    * 4. Repeat the step 1 until iteration of all elements
    */

    // Loop invariant : Elements till a[i - 1] are already sorted.
    for (int i = 0; i < n - 1; i++) {
        int min = i;

        // Find minimum element from arr[i] to arr[n - 1]
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }

        // Move minimum element at current i.
        int minElKey = arr[min];
        while (min > i) {
            arr[min] = arr[min - 1];
            min--;
        }
        arr[i] = minElKey;
    }
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

    vi arrCopy(arr); // will be used to demonstrate stable selection sort

    std::cout << "\nSorted elements via selection sort:\n";
    selectionSort(arr, n);
    printVector(arr);

    std::cout << "\nSorted elements via stable selection sort:\n";
    stableSelectionSort(arrCopy, n);
    printVector(arrCopy);

    return 0;
}