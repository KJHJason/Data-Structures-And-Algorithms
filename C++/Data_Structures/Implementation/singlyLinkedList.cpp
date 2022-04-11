#include <iostream>

/* ================================= SINGLY LINKED LIST IMPLEMENTATION CODES ================================= */

// Nodes for the singly linked list
class Node 
{
    public:
        int data;
        Node* next;

        // Default constructor if there's no arguments passed in
        Node()
        {
            data = 0;
            next = NULL;
        }

        // Constructor if there's a argument passed in
        Node(int data)
        {
            this->data = data;
            this->next = NULL;
        }
};

/*
    Singly Linked List is a data structure that consists of a group of nodes where each node contains data and a pointer to the next node in the list.

    It is a type of linked list that is unidirectornal in traversal. This means that we can only traverse the
    linked list from the left/head to the right.

    Methods Time Complexities:
    - searchPosByData: O(n)
    - searchPosByIndex: O(n)
    - insertToFront: O(1)
    - insertToBack: O(n)
    - insertAt: O(n)
    - deleteFrontNode: O(1)
    - deleteBackNode: O(n)
    - deleteNodeByData: O(n)
    - deleteNodeAt: O(n)
    - size: O(1)
    - reverseLinkedList: O(n)
    - printList: O(n)
*/
class LinkedList
{
    Node* head;
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
        void printLinkedList();
};

// destructor function to delete the linked list
LinkedList::~LinkedList() 
{ 
    Node* temp = head;
    Node* prev = NULL;

    while (temp != NULL) {
        prev = temp;
        temp = temp->next;
        delete prev;
    }
}

// function to search for a node position with the given data
int LinkedList::searchPosByData(int d)
{
    int pos{};
    Node* temp = head;

    while (temp != NULL) {
        if (temp->data == d) return pos;
        temp = temp->next;
        pos++;
    }

    return -1;
}

// function to search for a node data with the given position
int LinkedList::searchDataByPos(int pos)
{
    int count{};
    Node* temp = head;

    while (temp != NULL) {
        if (count == pos) return temp->data;
        temp = temp->next;
        count++;
    }

    return -1;
}

// function to add a node to the back of the linked list
void LinkedList::insertToBack(int data)
{
    Node* newNode = new Node(data);

    if (!head) {
        head = newNode;
    }
    else {
        Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    currentSize++;
}

// function to add a node to the front of the linked list
void LinkedList::insertToFront(int data)
{
    Node* newNode = new Node(data);

    if (!head) {
        head = newNode;
    }
    else {
        newNode->next = head;
        head = newNode;
    }
    currentSize++;
}

// function to add a node at a specific position (Note: 0 is the first position)
void LinkedList::insertAt(int data, int pos)
{
    Node* newNode = new Node(data);

    if (!head) {
        head = newNode;
    }
    else {
        Node* temp = head;
        int count = 0;
        while (temp->next != NULL && count < pos) {
            temp = temp->next;
            count++;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }
    currentSize++;
}

// function to delete the node at the head
void LinkedList::deleteFrontNode()
{
    if (!head) return;
    else {
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    currentSize--;
}

void LinkedList::deleteBackNode()
{
    if (!head) return;
    else {
        Node* temp = head;
        Node* prev = NULL;
        while (temp->next != NULL) {
            prev = temp;
            temp = temp->next;
        }
        prev->next = NULL;
        delete temp;
    }
    currentSize--;
}

// function to delete a node from the linked list by searching for the specified node with passed in data argument
void LinkedList::deleteNodeByData(int data)
{
    Node* temp = head;
    Node* prev = NULL;

    while (temp != NULL) {
        if (temp->data == data) {
            if (!prev) {
                head = temp->next;
            }
            else {
                prev->next = temp->next;
            }
            delete temp;
            currentSize--;
            break;
        }

        // if the node is not found, then move to the next node
        prev = temp;
        temp = temp->next;
    }
}

// function to delete a node from the linked list by searching for the specified node with passed in position argument (Note: 0 is the first position)
void LinkedList::deleteNodeAt(int index)
{
    Node* temp = head;
    Node* prev = NULL;
    int count = 0;

    while (temp != NULL) {
        if (count == index) {
            if (!prev) {
                head = temp->next;
            }
            else {
                prev->next = temp->next;
            }
            delete temp;
            currentSize--;
            break;
        }
        prev = temp;
        temp = temp->next;
        count++;
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
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}

// function to print the entire linked list
void LinkedList::printLinkedList()
{
    Node* temp = head;
    if (!temp) {
        std::cout << "Unable to print Linked list as it is empty!\n";
        return;
    }

    while (temp != NULL) {
        std::cout << temp->data << " ";
        temp = temp->next;
    }
    std::cout << "\n";
}

/* ================================= END OF SINGLY LINKED LIST IMPLEMENTATION ================================= */

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
    std::cout << "Demonstrating Singly Linked List Implementation:\n\n";
    demo();
    std::cout << "\nEnd of program...";
    return 0;
}