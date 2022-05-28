#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

typedef std::vector<int> vi;

bool is_sorted(const vi& arr, int n)
{
    for (int i = 1, n = arr.size(); i < n; i++) {
        if (arr[i-1] > arr[i]) 
            return false; // returns false if an element is smaller than the one to its left
    }
    return true;
}

void swap_two_random_elements(vi& arr, const int& n)
{
    int i{rand() % n}, j{rand() % n};
    std::swap(arr[i], arr[j]);
}

/*
    * Bozosort details: 

    * Best time complexity: O(n) when the array is already sorted
    * Worst time complexity: O(∞) as this algorithm has no upper bound
    * Average time complexity: O(n*n!)

    * Space complexity: O(1)
    
    * How it works:
    * 1. Randomly swap two elements in the array
    * 2. Repeat step 1 until the array is sorted

    * Note that this should be used as a joke or as a placeholder for a more efficient sorting algorithm since this sorting algorithm is very inefficient.
*/
void bozo_sort(vi& arr, int n)
{
    unsigned long long int count{};
    // randomly swap 2 elements in the array until it's sorted
    while (!is_sorted(arr, n)) {
        swap_two_random_elements(arr, n);
        count++;
    }
    std::cout << "\nBozo sort took " << count << " swappings to sort the array!\n";
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

    bozo_sort(arr, n);
    for (const auto& i: arr) std::cout << i << " ";
    return 0;
}