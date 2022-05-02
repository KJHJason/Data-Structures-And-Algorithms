#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

typedef std::vector<int> vi;

/*
    * Linear search for sorted arrays:
    * This is a search algorithm that works by taking each element one by one and comparing it with the element to be found.
    * Additionally, since the array is already sorted, this algorithm will check if the element at index i is bigger than the element to be found. 
    * If it is, then the element to be found is not present in the array.
    * If the element is found, the algorithm returns the index of the element.
    * As the name implies, the array must be sorted before this algorithm can be used.

    * Best time complexity: O(1)
    * Average time complexity: O(n)
    * Worst time complexity: O(n)
    * Space complexity: O(1)
*/
std::pair<int, int> sortedLinearSearch(const vi& arr, const int& elementToFind)
{
    int numOfComparison{};

    for (int i = 0; i < arr.size(); ++i) {
        numOfComparison++;
        // stop searching when element is found
        if (arr[i] == elementToFind) 
            return std::make_pair(i, numOfComparison);

        numOfComparison++;
        // stop searching if element is bigger than the element to be found
        if (arr[i] > elementToFind)
            return std::make_pair(-1, numOfComparison);
    }
    return std::make_pair(-1, numOfComparison);

}

/*
    * Optimised linear search:
    * This is a search algorithm that works by creating two pointers, one at the start of the array and one at the end of the array.
    * The pointers are moved towards each other until the element to be found is found or the pointers meet.
    * Hence, this algorithm will have more comparisons than a typical linear search algorithm.
    * Works for both sorted and unsorted arrays.

    * Best time complexity: O(1)
    * Average time complexity: O(n)
    * Worst time complexity: O(n)
    * Space complexity: O(1)
*/
std::pair<int, int> optimisedLinearSearch(const vi& arr, const int& elementToFind)
{
    int numOfComparison{};

    // create two pointers that point to the start and the end of the array
    int l{0}, r = arr.size() - 1;
    while (l <= r) {
        numOfComparison++;
        // stop searching when element is found on the left pointer
        if (arr[l] == elementToFind) 
            return std::make_pair(l, numOfComparison);
        
        numOfComparison++;
        // stop searching if element is found on the right pointer
        if (arr[r] == elementToFind) 
            return std::make_pair(r, numOfComparison);

        l++; r--;
    }
    return std::make_pair(-1, numOfComparison);
}

/*
    * Linear search:
    * This is a search algorithm that works by taking each element one by one and comparing it with the element to be found.
    * Works for both sorted and unsorted arrays.

    * Best time complexity: O(1)
    * Average time complexity: O(n)
    * Worst time complexity: O(n)
    * Space complexity: O(1)
*/
std::pair<int, int> linearSearch(const vi& arr, const int& elementToFind)
{   
    int numOfComparison{};

    for (int i = 0; i < arr.size(); ++i) {
        numOfComparison++;
        if (arr[i] == elementToFind)
            return std::make_pair(i, numOfComparison);
    }
    return std::make_pair(-1, numOfComparison);
}

// function to check if the input contains only numbers
bool validateInput(std::string &str)
{
    if (str.empty())
        return 0;

    for (const auto &c : str)
        if (!isdigit(c) && c != ' ' && c != '-')
            return 0;

    return 1;
}

int main()
{
    vi arr; std::string str;
    while (1) {
        std::cout << "Enter elements (with spaces as the delimiter):\n";
        std::getline(std::cin, str);
        if (validateInput(str))
            break;
        else 
            std::cout << "Please enter only integers!\n\n";
    }

    // convert string to a vector of integers
    std::stringstream ss(str); int i;
    while (ss >> i)
        arr.push_back(i);

    int x;
    std::cout << "\nEnter element to find:\n";
    std::cin >> x;

    // demonstrating linear search
    std::cout << "\nSearching using linear search...\n";
    std::pair<int, int> foundIndexPair0 = linearSearch(arr, x);
    if (foundIndexPair0.first == -1)
        std::cout << "Element not found " << foundIndexPair0.second << " comparison(s)\n";
    else
        std::cout << "Element found at index " << foundIndexPair0.first << " after " << foundIndexPair0.second << " comparison(s)\n";

    // demonstrating optmised linear search
    std::cout << "\nSearching using optimised linear search...\n";
    std::pair<int, int> foundIndexPair1 = optimisedLinearSearch(arr, x);
    if (foundIndexPair1.first == -1)
        std::cout << "Element not found " << foundIndexPair1.second << " comparison(s)\n";
    else
        std::cout << "Element found at index " << foundIndexPair1.first << " after " << foundIndexPair1.second << " comparison(s)\n";

    // sorting the array for the next linear search algorithm demonstration
    std::cout << "\nSorting array...";
    std::sort(arr.begin(), arr.end());

    std::cout << "\x1b[2K"; // clear entire line
    std::cout << "\rSorted Array:\n";
    for (const auto& i: arr) 
        std::cout << i << " "; 
    std::cout << "\n";

    // demonstrating linear search for sorted arrays
    std::cout << "\nSearching using linear search for sorted arrays...\n";
    std::pair<int, int> foundIndexPair2 = sortedLinearSearch(arr, x);
    if (foundIndexPair2.first == -1)
        std::cout << "Element not found after " << foundIndexPair2.second << " comparison(s)\n";
    else
        std::cout << "Element found at index " << foundIndexPair2.first << " after " << foundIndexPair2.second << " comparison(s)\n";

    return 0;
}