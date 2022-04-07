#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

std::vector<int> bubbleSort(std::vector<int> arr, int n)
{
    /*
    * Bubble sort details:
    Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.

    * Best time complexity: O(n) when the array is already sorted.
    * Average time complexity: O(n^2)
    * Worst time complexity: O(n^2)

    * Space complexity: O(1)

    * How it works: 
    * 1. Compare the first element with the second element.
    * 2. If the first element is greater than the second element, swap them.
    * 3. Repeat the entire process for the next two elements.

    * Note that there is the boolean flag variable to optimise it to O(n) best time complexity 
    for the best case scenario where the array is already sorted in the first iteration.
    * The flag is implemented to break out of the loop after an iteration that had no swapping.
    */
    bool flag = false;
    for (int i=0; i < n; i++) {
        for (int j=0; j < n-1; j++) {
            if (arr[j] > arr[j+1]) {
                std::swap(arr[j], arr[j+1]);
                flag = true;
            }
        }
        if (!flag) break;
    }
    return arr;
}

int main()
{
    std::vector<int> arr;
    std::cout << "Enter number of elements: ";
    int n; std::cin >> n;
    std::cout << "\n";

    std::cout << "Enter elements (with spaces as the delimiter):\n";
    for (int i=0; i < n; i++) {
        int x; std::cin >> x;
        arr.push_back(x);
    }

    std::cout << "\nSorted elements:\n";
    arr = bubbleSort(arr, n);
    for (auto i: arr) {
        std::cout << i << " ";
    }
    return 0;
}