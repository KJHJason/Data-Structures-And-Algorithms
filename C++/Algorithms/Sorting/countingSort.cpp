#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

/*
    * Counting sort details:
    The counting sort algorithm sorts an array by counting the number of occurrences of each element.
    It is a linear time algorithm in the worst case.

    * Best time complexity: O(n+k) where k is the range
    * Worst time complexity: O(n+k) where k is the range
    * Average time complexity: O(n+k) where k is the range

    * Space complexity: O(n+k) where k is the range

    * How it works: 
    * 1. Find minimum and maximum values in the array
    * 2. Create a count array of size (maximum - minimum + 1) with all values as 0
    * 3. For each element in the input array, increment the count array at the index of the element
    * 4. Change the count array to the cumulative sum of the elements
    * 5. Create a new array as a placeholder for the sorted array
    * 6. Find the index of each element of the original array in count array, and place the elements in the new array
*/
void countingSort(vi& arr, int n)
{
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min + 1;
    vi countArr(range, 0);

    // storing count of each element
    for (int i = 0; i < n; i++) {
        countArr[arr[i] - min]++;
    }

    // changing countArr to store the cumulative sum of the elements
    // e.g. [1, 0, 2, 0 , 1], meaning the input array was [1, 3, 3, 5], based on the count of each element
    // to [1, 1, 3, 3, 4] based on the cumulative sum of each element
    for (int i = 1; i < range; i++) {
        countArr[i] += countArr[i - 1];
    }

    vi sortedArr(n);
    for (int i = n - 1; i >= 0; i--) {
        // Find the correct index in the sorted array, and place the element there
        sortedArr[countArr[arr[i] - min] - 1] = arr[i];
        // decrement the countArr count value
        countArr[arr[i] - min]--; 
    }
    arr = sortedArr;
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
    countingSort(arr, n);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}