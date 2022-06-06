#include <iostream>
#include <forward_list>

// print a new line
void nl()
{
    std::cout << "\n";
}

void printList(std::forward_list<int> &l)
{
    if (!l.empty()) {
        for (auto i : l) {
            std::cout << i << " ";
        }
    }
    else std::cout << "Unable to print as the linked list is empty!";
    nl();
}

bool evenCheck(const int& i); // forward declaration of a demo seen at the end of demo function

/*
    Singly Linked List is a data structure that consists of a group of nodes where each node contains data and a pointer to the next node in the list.

    It is a type of linked list that is unidirectornal in traversal. This means that we can only traverse the
    linked list from the left/head to the right.

    Note: This demo uses C++'s STL forward list sequence container to demonstrate the functionality of a singly linked list.
    More details: https://www.geeksforgeeks.org/list-cpp-stl/
*/
void demo()
{
    std::cout << "Creating a linked list with 5 elements:\n";
    std::forward_list<int> l;
    // .push_front() to add data to the front of the list
    l.push_front(10);
    l.push_front(20);
    l.push_front(30);
    l.push_front(40);
    l.push_front(50);
    printList(l);

    // .front() to get the first element of the list
    std::cout << "First element of the linked list: " << l.front() << "\n";

    // .size() to get the size of the list
    std::cout << "Size of the linked list: ";
    int count{};
    for (auto i : l) {
        count++;
    }
    std::cout << count << "\n";

    // .empty() to check if the list is empty
    std::cout << "Is the linked list empty? " << (l.empty() ? "Yes" : "No") << "\n";

    // .clear() to clear the list
    nl();
    std::cout << "Clearing the linked list..." << "\n";
    l.clear();
    std::cout << "Is the linked list empty? " << (l.empty() ? "Yes" : "No") << "\n";
    
    // .assign() to assign new elements to the list (overwrites the existing elements if any)
    nl();
    std::cout << "Adding back the elements to the list...\n";
    l.assign({11, 10, 19, 20, 30, 40, 40, 40, 50, 50});
    printList(l);

    // .advance to point to nth position and .insert() to insert data to it
    nl();
    std::cout << "Inserting data at position 2...\n";
    std::forward_list<int>::iterator it = l.begin();
    std::advance(it, 2);
    l.insert_after(it, 25);
    printList(l);

    // .erase() to remove data from the list
    nl();
    std::cout << "Removing data at position 2...\n";
    it = l.begin();
    std::advance(it, 2);
    l.erase_after(it);
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
    std::forward_list<int> l2;
    l2.assign({60, 70, 80, 90});
    printList(l2);
    
    std::cout << "Merging the two linked lists...\n";
    l.merge(l2);
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