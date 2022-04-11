#include <iostream>

/* ================================= DOUBLY LINKED LIST IMPLEMENTATION CODES ================================= */

// Nodes for the doubly linked list
class Node 
{
    public:
        int data;
        Node* next;
        Node* prev;

        // Default constructor if there's no arguments passed in
        Node()
        {
            data = 0;
            next = NULL;
            prev = NULL;
        }

        // Constructor if there's a argument passed in
        Node(int data)
        {
            this->data = data;
            this->next = NULL;
            this->prev = NULL;
        }
};

/*
    Doubly linked list is a data structure that consists of a group of nodes that are linked together
    where each node contains data and a pointer to the next and previous node in the linked list.

    It is a type of linked list that is bidirectional in traversal. This means that we can traverse the
    linked list from the head/left to the tail/right or vice versa.

    Methods Time Complexities:
    - searchPosByData: O(n)
    - searchPosByIndex: O(n)
    - insertToFront: O(1)
    - insertToBack: O(1)
    - insertAt: O(n)
    - deleteFrontNode: O(1)
    - deleteBacwkNode: O(1)
    - deleteNodeByData: O(n)
    - deleteNodeAt: O(n)
    - size: O(1)
    - reverseLinkedList: O(n)
    - printLinkedList: O(n)
*/
class LinkedList
{
    Node* head;
    Node* tail;
    int currentSize{};

    public:
        LinkedList() { head = NULL; }
        ~LinkedList();

        int searchPosByData(int d);
        int searchDataByPos(int pos);

        void insertToFront(int d);
        void insertToBack(int d);
        void insertAt(int d, int pos);

        void deleteFrontNode();
        void deleteBackNode();
        void deleteNodeByData(int d);
        void deleteNodeAt(int pos);

        int size();
        void reverseLinkedList();
        void printLinkedList(bool printReverse = 0);
};

// destructor function to delete the linked list
LinkedList::~LinkedList() 
{ 
    Node* temp = head;
    while (temp != NULL) {
        Node* next = temp->next;
        delete temp;
        temp = next;
    }
}

// function to search for a node position with the given data
int LinkedList::searchPosByData(int d)
{
    int pos{};
    Node* temp = head;

    while (temp != NULL) {
        if (temp->data == d) return pos;
        pos++;
        temp = temp->next;
    }

    return -1;
}

// function to search for a node data with the given position
int LinkedList::searchDataByPos(int pos)
{
    if (!head) return -1;

    int mid = (currentSize - 1) / 2; // -1 to account for the indexing starting from 0
    int count;
    if (pos > mid) {
        count = currentSize - 1;
        Node* temp = tail;
        while (count >= pos) {
            if (count == pos) return temp->data;
            temp = temp->prev;
            count--;
        }
    } else {
        count = 0;
        Node* temp = head;
        while (count <= pos) {
            if (count == pos) return temp->data;
            temp = temp->next;
            count++;
        }
    }
    
    return -1; // if the position is out of bound
}

// function to add a node to the back of the linked list
void LinkedList::insertToBack(int data)
{
    Node* newNode = new Node(data);

    if (!head) {
        head = newNode;
        tail = newNode;
    } 
    else {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }

    currentSize++;
}

// function to add a node to the front of the linked list
void LinkedList::insertToFront(int data)
{
    Node* newNode = new Node(data);

    if (!head) {
        head = newNode;
        tail = newNode;
    } 
    else {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }

    currentSize++;
}

// function to add a node at a specific position (Note: 0 is the first position)
void LinkedList::insertAt(int data, int pos)
{
    if (pos == 0) insertToFront(data); 
    else if (pos == currentSize) insertToBack(data);
    else {
        Node* newNode = new Node(data);
        Node* temp = head;
        int count = 0;

        while (count < pos) {
            temp = temp->next;
            count++;
        }

        newNode->next = temp;
        newNode->prev = temp->prev;
        temp->prev->next = newNode;
        temp->prev = newNode;

        currentSize++;
    }
}

// function to delete the node at the head, aka the first node on the left
void LinkedList::deleteFrontNode()
{
    if (!head) return;

    Node* temp = head;
    head = head->next;
    head->prev = NULL;
    delete temp;

    currentSize--;
}

// function to delete the node at the back, aka the last node on the right
void LinkedList::deleteBackNode()
{
    if (!head) return;

    Node* temp = tail;
    tail = tail->prev;
    tail->next = NULL;
    delete temp;

    currentSize--;
}

// function to delete a node from the linked list by searching for the specified node with passed in data argument
void LinkedList::deleteNodeByData(int data)
{
    if (!head) return;

    Node* temp = head;
    while (temp != NULL) {
        if (temp->data == data) {
            if (temp == head) deleteFrontNode();
            else if (temp == tail) deleteBackNode();
            else {
                temp->prev->next = temp->next;
                temp->next->prev = temp->prev;
                delete temp;
                currentSize--;
            }
            break;
        }
        temp = temp->next;
    }
}

// function to delete a node from the linked list by searching for the specified node with passed in position argument (Note: 0 is the first position)
void LinkedList::deleteNodeAt(int index)
{
    if (!head) return;

    Node* temp = head;
    int count{};

    while (count < index) {
        temp = temp->next;
        count++;
    }

    if (temp == head) deleteFrontNode();
    else if (temp == tail) deleteBackNode();
    else {
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        delete temp;
        currentSize--;
    }
}

// function to return the size of the linked list
int LinkedList::size()
{
    return currentSize;
}

// function to reverse the entire linked list
void LinkedList::reverseLinkedList()
{
    if (!head) return;
    Node* headCopy = head;

    Node* temp = head;
    Node* prev = NULL;
    Node* next = NULL;

    while (temp != NULL) {
        next = temp->next;
        temp->next = prev;
        temp->prev = next;
        prev = temp;
        temp = next;
    }

    head = prev;
    tail = headCopy;
}

// function to print the entire linked list
void LinkedList::printLinkedList(bool printReverse)
{
    if (!head) {
        std::cout << "Unable to print Linked list as it is empty!\n";
        return;
    }

    if (printReverse) {
        Node* temp = tail;
        while (temp != NULL) {
            std::cout << temp->data << " ";
            temp = temp->prev;
        }
    } else {
        Node* temp = head;
        while (temp != NULL) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
    }
    std::cout << "\n";
}

/* ================================= END OF DOUBLY LINKED LIST IMPLEMENTATION ================================= */

void br()
{
    std::cout << "\n";
}

void demo()
{
    // initialise a linked list
    std::cout << "Creating a linked list with 5 elements:\n";
    LinkedList list;
    list.insertToBack(10);
    list.insertToBack(20);
    list.insertToBack(30);
    list.insertToBack(40);
    list.insertToBack(50);
    list.printLinkedList();
    std::cout << "Size of linked list: " << list.size() << "\n";

    // searching
    br();
    std::cout << "Searching for node position with data = 30: " << list.searchPosByData(30) << "\n";
    std::cout << "Searching for node data with position = 2: " << list.searchDataByPos(2) << "\n";

    // reversing linked list
    br();
    std::cout << "Reversing the linked list:\n";
    list.reverseLinkedList();
    list.printLinkedList();

    // insertion
    br();
    std::cout << "Inserting a new element, 60, at the back of the list:\n";
    list.insertToBack(60);
    list.printLinkedList();

    br();
    std::cout << "Inserting a new element, 70, at the front of the list:\n";
    list.insertToFront(70);
    list.printLinkedList();

    br();
    std::cout << "Inserting a new element, 80, at the position 1 of the list:\n";
    list.insertAt(80, 1);
    list.printLinkedList();

    // deletion
    br();
    std::cout << "Deleting the first element of the list:\n";
    list.deleteFrontNode();
    list.printLinkedList();

    br();
    std::cout << "Deleting the last element of the list:\n";
    list.deleteBackNode();
    list.printLinkedList();

    br();
    std::cout << "Deleting the node with data = 40 from the list:\n";
    list.deleteNodeByData(40);
    list.printLinkedList();

    br();
    std::cout << "Deleting the element at the position 1 of the list:\n";
    list.deleteNodeAt(1);
    list.printLinkedList();
}

int main()
{
    std::cout << "Demonstrating Doubly Linked List Implementation:\n\n";
    demo();
    std::cout << "\nEnd of program...";
    return 0;
}