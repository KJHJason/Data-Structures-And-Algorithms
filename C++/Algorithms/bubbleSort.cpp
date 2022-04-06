#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

typedef std::int_fast32_t fint32;
typedef std::int_fast64_t fint64;

void bubbleSort(std::vector<fint64> arr)
{
    for (int i=0; i < n; i++) {

    }
}

int main()
{
    std::vector<fint64> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::vector<fint64> sortedArr = bubbleSort(arr);
    for (int i=0; i < n; i++) {
        std::cout << sortedArr[i] << " ";
    }
    return 0;
}