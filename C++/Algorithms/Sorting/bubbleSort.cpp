#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

/*
    * Bubble sort details:
    Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.

    * Best time complexity: O(n) when the array is already sorted.
    * Worst time complexity: O(n^2)
    * Average time complexity: O(n^2)

    * Space complexity: O(1)

    * How it works: 
    * 1. Compare the first element with the second element.
    * 2. If the first element is greater than the second element, swap them.
    * 3. Repeat the entire process for the next two elements.

    * Note that there is the boolean flag variable to optimise it to O(n) best time complexity 
    for the best case scenario where the array is already sorted in the first iteration.
    * The flag is implemented to break out of the loop after an iteration that had no swapping.
*/
void bubbleSort(vi& arr, int n)
{
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
    bubbleSort(arr, n);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}