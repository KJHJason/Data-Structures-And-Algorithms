#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

/*
    * Dutch National Flag Algorithm/3-way Partitioning Algorithm Details:
    The Dutch National Flag algorithm or the 3-way partitioning algorithm is an
    algorithm that uses a pivot value (starting from the left/index 0) to divide an array 
    into three parts where the first subarray will contain elements of 0 and 
    the second subarray will contain elements of 1 and the third subarray will elements of 2.
    The algorithm is used in various sorting algorithms such as the 3-way quick sort algorithm.
    This sorting algorithm sort the array with elements among the 3 numbers (0, 1, 2) in an ascending order.

    * Best time complexity: O(n)
    * Worst time complexity: O(n)
    * Average time complexity: O(n)

    * Space complexity: O(1)
    */
void sort(vi& arr, int n)
{
    // initialise pointers
    int low{}, mid {}, high{n - 1};

    while (mid <= high) {
        switch (arr[mid]) {
            case 0:
                // note that low++ and mid++ will increment after the swap as it is a post-increment
                std::swap(arr[low++], arr[mid++]); 
                break;
            case 1:
                mid++;
                break;
            case 2:
                // note that high-- will decrement after the swap as it is a post-decrement
                std::swap(arr[mid], arr[high--]);
                break;
            default:
                std::cout << "\nElement is not between 0 to 2!\n";
                return;
        }
    }
}

int main()
{
    vi arr;
    std::cout << "Enter number of elements: ";
    int n; std::cin >> n;
    std::cout << "\n";

    std::cout << "Enter elements (with spaces as the delimiter and elements between 0 to 2):\n";
    for (int i=0; i < n; i++) {
        int x; std::cin >> x;
        arr.push_back(x);
    }

    std::cout << "\nSorted elements:\n";
    sort(arr, n);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}