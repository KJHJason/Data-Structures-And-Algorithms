#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> vi;

void merge(vi& arr, const int left, const int mid, const int right)
{
    const int leftArrSize = mid - left + 1;
    vi leftArr(leftArrSize);

    const int rightArrSize = right - mid;
    vi rightArr(rightArrSize);

    // copy data from arr to the two temporary arrays
    for (int i = 0; i < leftArrSize; ++i) {
        leftArr[i] = arr[left + i];
    }
    for (int i = 0; i < rightArrSize; ++i) {
        rightArr[i] = arr[mid + 1 + i];
    }

    // create int variables to store the initial index of the two temporary arrays and the merged array
    int indexOfLeftArr{}, indexOfRightArr{}, indexOfMergedArr{left};

    // merge the two temporary arrays while comparing the elements from the two temporary arrays
    while (indexOfLeftArr < leftArrSize && indexOfRightArr < rightArrSize) {
        // if the element in the left array is smaller than the element in the right array, 
        // then copy the element from the left array to the merged array
        if (leftArr[indexOfLeftArr] <= rightArr[indexOfRightArr]) 
        {
            arr[indexOfMergedArr] = leftArr[indexOfLeftArr];
            indexOfLeftArr++;
        } 
        // if the element in the left array is larger than the element in the right array, 
        // then copy the element from the right array to the merged array
        else 
        {
            arr[indexOfMergedArr] = rightArr[indexOfRightArr];
            indexOfRightArr++;
        }
        indexOfMergedArr++;
    }

    // copy any remaining elements of the temporary arrays to the merged array
    while (indexOfLeftArr < leftArrSize) {
        arr[indexOfMergedArr] = leftArr[indexOfLeftArr];
        indexOfLeftArr++;
        indexOfMergedArr++;
    }
    while (indexOfRightArr < rightArrSize) {
        arr[indexOfMergedArr] = rightArr[indexOfRightArr];
        indexOfRightArr++;
        indexOfMergedArr++;
    }
}

/*
    * Merge Sort Details:
    * This is a sorting algorithm that works by dividing the array into two parts and sorting them recursively (divide and conquer).
    * The algorithm then merges the two sorted parts to form the final sorted array.
    * This algorithm is stable.

    * Best time complexity: O(n log n)
    * Worst time complexity: O(n log n)
    * Average time complexity: O(n log n)

    * Space complexity: O(n)

    * How it works:
    * 1. The algorithm starts by dividing the array into two parts
    * 2. Then it sorts the two parts recursively
    * 3. Then it merges the two sorted parts to form the final sorted array
*/
void mergeSort(vi& arr, const int start, const int end)
{
    if (start >= end) return; // if the array has LESS THAN 2 elements (x < 2), there is nothing to sort

    int mid = start + (end - start) / 2;
    mergeSort(arr, start, mid); // sort the left half
    mergeSort(arr, mid + 1, end); // sort the right half
    merge(arr, start, mid, end); // merge the two halves
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
    mergeSort(arr, 0, n - 1);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}