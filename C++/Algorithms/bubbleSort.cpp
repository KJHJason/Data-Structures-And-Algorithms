#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

typedef std::int_fast32_t fint32;
typedef std::int_fast64_t fint64;

std::vector<fint64> bubbleSort(std::vector<fint64> arr, int n)
{
    /*
    * Bubble Sort Details
    * Best time complexity: O(n) when the array is already sorted.
    * Average time complexity: O(n^2)
    * Worst time complexity: O(n^2)
    * Space complexity: O(1)

    * How it works: 
    * 1. Compare the first element with the second element.
    * 2. If the first element is greater than the second element, swap them.
    * 3. Repeat the entire process for the next two elements.

    * Note that there is flag boolean to optimise bubble sort so that it 
    will break out of the loop when the array has been sorted after an iteration that had no swapping.
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
    std::vector<fint64> arr;
    std::cout << "Enter number of elements: ";
    int n; std::cin >> n;
    std::cout << "\n";

    std::cout << "Enter elements (with spaces as the delimiter):\n";
    for (int i=0; i < n; i++) {
        fint64 x; std::cin >> x;
        arr.push_back(x);
    }

    std::cout << "\nSorted elements:\n";
    arr = bubbleSort(arr, n);
    for (auto i: arr) {
        std::cout << i << " ";
    }
    return 0;
}