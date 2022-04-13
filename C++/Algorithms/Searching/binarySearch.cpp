#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

typedef std::vector<std::string> vs;

/*
    * Iterative Binary Search Details:
    * This is a search algorithm that works by dividing the array into two parts, the left part and the right part.
    * The left part contains all the elements that are smaller than the element to be found.
    * The right part contains all the elements that are larger than the element to be found.
    * The algorithm then repeats the process until the element is found or the left part is empty.

    * Best time complexity: O(1)
    * Average time complexity: O(log n)
    * Worst time complexity: O(log n)
    * Space complexity: O(1)
*/
int iterativeBinarySearch(const vs& arr, const std::string& elementToFind, int& l, int& r)
{
    while (l <= r) {
        int mid = l + (r - l) / 2;

        // Check if elementToFind is present at mid
        if (arr[mid] == elementToFind) return mid;

        // If elementToFind greater, ignore left half
        if (arr[mid] < elementToFind) l = mid + 1;

        // If elementToFind is smaller, ignore right half
        else r = mid - 1;
    }

    return -1; // return -1 if element is not present
}

/*
    * Recursive Binary Search Details:
    * Same as the iterative binary search algorithm, but this algorithm is recursive.
    * This is a search algorithm that works by dividing the array into two parts, the left part and the right part.
    * The left part contains all the elements that are smaller than the element to be found.
    * The right part contains all the elements that are larger than the element to be found.
    * The algorithm then repeats the process until the element is found or the left part is empty.
    * The algorithm is recursive because it calls itself.

    * Best time complexity: O(1)
    * Average time complexity: O(log n)
    * Worst time complexity: O(log n)
    * Space complexity: O(1)
*/
int recursiveBinarySearch(const vs& arr, const std::string& elementToFind, int l, int r)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;

        // If the element is present at the middle
        if (arr[mid] == elementToFind) return mid;

        // If element is smaller than mid, then it can only be present in left subarray
        if (arr[mid] > elementToFind) return recursiveBinarySearch(arr, elementToFind, l, mid - 1);

        // Else the element can only be present in right subarray
        return recursiveBinarySearch(arr, elementToFind, mid + 1, r);
    }

    return -1; // return -1 if element does not exist in array
}

// function to convert string to lowercase
void lowercase(std::string &str)
{
    std::transform(str.begin(), str.end(), str.begin(), ::tolower);
}

int main()
{
    vs arr;

    std::string promptInput;
    while (1) {
        std::cout << "Do you want to manually enter elements or randomly generate nth numbers of elements?\n";
        std::cout << "Enter \"y\" to manually enter or \"n\" to generate nth numbers of elements: ";
        std::cin >> promptInput;
        lowercase(promptInput);
        if (promptInput == "y" || promptInput == "n") {
            break;
        }
        else {
            std::cout << "Invalid input. Please enter \"y\" or \"n\"!\n\n";
            continue;
        }
    }

    if (promptInput == "y") {
        std::cout << "\nPlease enter elements in this format:\nelement1 element2 element2 (with spaces as the delimiter)\nx (finally enter x to stop)\n\n";
        std::cout << "Enter elements for searching later (x to stop):\n";
        while (1) {
            std::string x; std::cin >> x;
            lowercase(x);
            if (x == "x") break;
            arr.push_back(x);
        }
    }
    else {
        std::cout << "\nPlease enter the number of elements you want to generate: ";
        int n; std::cin >> n;
        std::cout << "Elements generated:\n";
        for (int i = 0; i < n; i++) {
            int ran = std::rand() % 1000 + 1;
            arr.push_back(std::to_string(ran));
            std::cout << ran << " ";
        }
        std::cout << "\n";
    }
    
    std::sort(arr.begin(), arr.end());

    int n = arr.size();
    int l = 0; 
    int r = n - 1; // -1 to account for indexing

    std::cout << "\nEnter the element to search for: ";
    std::string s; std::cin >> s;
    lowercase(s);

    if (iterativeBinarySearch(arr, s, l, r) != -1) {
        std::cout << "Element found: " << s << " via iterative binary search\n";
    } else {
        std::cout << "Element \"" << s << "\" not found\n";
    }

    if (recursiveBinarySearch(arr, s, l ,r) != -1) {
        std::cout << "Element found: " << s << " via recursive binary search\n";
    } else {
        std::cout << "Element \"" << s << "\" not found\n";
    }
    return 0;
}