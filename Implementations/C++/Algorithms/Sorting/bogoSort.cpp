#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

typedef std::vector<int> vi;

bool isSorted(const vi& arr, int n)
{
    for (int i = 1, n = arr.size(); i < n; i++) {
        if (arr[i-1] > arr[i]) return false; // returns false if an element is smaller than the one to its left
    }
    return true;
}

void shuffle(vi& arr, int n)
{
    for (int i=0; i < n; i++) {
        int j = std::rand() % n; // pick a random index in the array
        std::swap(arr[i], arr[j]); // swap elements in the array with index j which was randomly chosen
    }
}

/*
    * Bogosort details: 
    Bogosort is a sorting algorithm that works by repeatedly shuffling a list of elements until it is in the correct order.

    * Best time complexity: O(n) when the array is already sorted
    * Worst time complexity: O(∞) as this algorithm has no upper bound
    * Average time complexity: O(n*n!)

    * Space complexity: O(1)
    
    * How it works:
    * 1. Shuffle the array
    * 2. Repeat step 1 until the array is sorted

    * Note that this should be used as a joke or as a placeholder for a more efficient sorting algorithm since this sorting algorithm is very inefficient.
*/
void bogoSort(vi& arr, int n)
{
    unsigned long long int count{};
    // shuffle the array until it's sorted
    while (!isSorted(arr, n)) {
        shuffle(arr, n);
        count++;
    }
    std::cout << "\nBogo sort took " << count << " shuffles to sort the array!\n";
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

    bogoSort(arr, n);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}