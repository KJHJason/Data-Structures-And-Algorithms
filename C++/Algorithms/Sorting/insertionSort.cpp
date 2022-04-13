#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

/*
    * Insertion sort details:
    The insertion sort algorithm sorts an array by taking each element one by one and placing it in its correct position in the sorted array.
    
    * Best time complexity: O(n)
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n^2)
    
    * Space complexity: O(1)
    
    * How it works: 
    * 1. Take each element in the array and place it in its correct position in the sorted array
    * 2. Repeat step 1 until the array is sorted
*/
void insertionSort(vi& arr, int n)
{
    for (int i = 1; i < n; i++) {
        int el = arr[i]; // save the value to be positioned

        int j = i - 1;
        
        // Move all the elements greater than int variable el by one index to the right ahead of their current position
        while (j >= 0 && arr[j ] > el) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = el;
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

    std::cout << "\nSorted elements:\n";
    insertionSort(arr, n);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}