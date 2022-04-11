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

// Singly linked list class
class LinkedList
{
    Node* head;

    public:
        LinkedList() { head = NULL; }

        void insertToFront(int d);
        void insertToBack(int d);
        void insertAt(int d, int pos);

        void deleteNode(int d);
        void deleteNodeAt(int pos);
        void deleteList();
        
        void reverseList();
        void printLinkedList();
};

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
}

// function to reverse the entire linked list
void LinkedList::reverseList()
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

// function to delete a node from the linked list by searching for the specified node with passed in data argument
void LinkedList::deleteNode(int data)
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
            break;
        }
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
            break;
        }
        prev = temp;
        temp = temp->next;
        count++;
    }
}

// function to delete the entire linked list
void LinkedList::deleteList()
{
    Node* temp = head;
    Node* prev = NULL;

    while (temp != NULL) {
        prev = temp;
        temp = temp->next;
        delete prev;
    }
    head = NULL;
}

/* ================================= END OF SINGLY LINKED LIST IMPLEMENTATION ================================= */

void br()
{
    std::cout << "\n";
}

void demo()
{
    std::cout << "Creating a linked list with 5 elements:\n";
    LinkedList list;
    list.insertToBack(10);
    list.insertToBack(20);
    list.insertToBack(30);
    list.insertToBack(40);
    list.insertToBack(50);
    list.printLinkedList();

    br();
    std::cout << "Reversing the linked list:\n";
    list.reverseList();
    list.printLinkedList();

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

    br();
    std::cout << "Deleting the first element of the list:\n";
    list.deleteNode(70);
    list.printLinkedList();

    br();
    std::cout << "Deleting the last element of the list:\n";
    list.deleteNode(60);
    list.printLinkedList();

    br();
    std::cout << "Deleting the element at the position 1 of the list:\n";
    list.deleteNodeAt(1);
    list.printLinkedList();

    br();
    std::cout << "Deleting the entire list:\n";
    list.deleteList();
    list.printLinkedList();
}

int main()
{
    std::cout << "Demonstrating Singly Linked List Implementation:\n\n";
    demo();
    std::cout << "\nEnd of program...";
    return 0;
}