#include <iostream>
#include <list>
#include <algorithm>

// print a new line
void nl()
{
    std::cout << "\n";
}

void printList(std::list<int> &l)
{
    if (!l.empty()) {
        for (auto it = l.begin(); it != l.end(); it++) {
            std::cout << *it << " ";
        }
    }
    else std::cout << "Unable to print as the linked list is empty!\n";
    nl();
}

bool evenCheck(const int& i); // forward declaration of a demo seen at the end of demo function

/*
    Doubly linked list is a data structure that consists of a group of nodes that are linked together
    where each node contains data and a pointer to the next and previous node in the linked list.

    It is a type of linked list that is bidirectional in traversal. This means that we can traverse the
    linked list from the head/left to the tail/right or vice versa.

    Note: This demo uses C++'s STL list data structure to demonstrate the functionality of a doubly linked list.
    More details: https://www.geeksforgeeks.org/list-cpp-stl/
*/
void demo()
{
    std::cout << "Creating a linked list with 5 elements:\n";
    std::list<int> l;
    // .push_front() to add data to the front of the list
    l.push_front(10);

    // .push_back() to add data to the back of the list
    l.push_back(20);
    l.push_back(30);
    l.push_back(40);
    l.push_back(50);
    printList(l);

    // .front() to get the first element of the list
    std::cout << "First element of the linked list: " << l.front() << "\n";

    // .back() to get the last element of the list
    std::cout << "Last element of the linked list: " << l.back() << "\n";

    // .size() to get the size of the list
    std::cout << "Size of the linked list: " << l.size() << "\n";

    // .empty() to check if the list is empty
    std::cout << "Is the linked list empty? " << (l.empty() ? "Yes" : "No") << "\n";

    // .clear() to clear the list
    nl();
    std::cout << "Clearing the linked list..." << "\n";
    l.clear();
    std::cout << "Is the linked list empty? " << (l.empty() ? "Yes" : "No") << "\n";
    
    nl();
    std::cout << "Adding back the elements to the list...\n";
    l.push_back(11);
    l.push_back(10);
    l.push_back(19);
    l.push_back(20);
    l.push_back(30);
    l.push_back(40);
    l.push_back(40);
    l.push_back(40);
    l.push_back(50);
    l.push_back(50);
    printList(l);

    // .advance to point to nth position and .insert() to insert data to it
    nl();
    std::cout << "Inserting data at position 2...\n";
    std::list<int>::iterator it = l.begin();
    std::advance(it, 2);
    l.insert(it, 25);
    printList(l);

    // .erase() to remove data from the list
    nl();
    std::cout << "Removing data at position 2...\n";
    it = l.begin();
    std::advance(it, 2);
    l.erase(it);
    printList(l);

    // .remove() to remove data from the list
    nl();
    std::cout << "Removing all data with the number 50...\n";
    l.remove(50);
    printList(l);

    // .reverse() to reverse the list
    nl();
    std::cout << "Reversing the linked list...\n";
    l.reverse();
    printList(l);

    // .sort() to sort the list
    nl();
    std::cout << "Sorting the linked list...\n";
    l.sort();
    printList(l);

    // .unique() to remove duplicate elements from the list
    nl();
    std::cout << "Removing duplicate elements from the linked list...\n";
    l.unique();
    printList(l);

    // .merge() to merge two lists
    nl();
    std::cout << "Creating another linked list...\n";
    std::list<int> l2;
    l2.push_back(60);
    l2.push_back(70);
    l2.push_back(80);
    l2.push_back(90);
    printList(l2);
    
    std::cout << "Merging the two linked lists...\n";
    l.merge(l2);
    printList(l);

    // .splice() to splice two lists/transfer elements from one linked list to another
    nl();
    std::cout << "Creating another linked list...\n";
    std::list<int> l3;
    l3.push_back(100);
    l3.push_back(110);
    l3.push_back(120);
    l3.push_back(130);
    printList(l3);

    std::cout << "Splicing the two linked lists...\n";
    l.splice(l.begin(), l3);
    printList(l);

    // .remove_if() to remove elements from the list
    nl();
    std::cout << "Removing elements if elements are even numbers from the list...\n";
    l.remove_if(evenCheck);
    printList(l);
}

// function to check if the element is even
bool evenCheck(const int& i)
{
    return (i % 2) == 0;
}

int main()
{
    std::cout << "Demonstrating Singly Linked List Implementation using C++ STL:\n\n";
    demo();
    std::cout << "\nEnd of program...";
    return 0;
}