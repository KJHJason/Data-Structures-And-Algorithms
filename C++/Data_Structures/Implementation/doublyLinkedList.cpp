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
    - get_pos: O(n)
    - get_data: O(n)
    - push_front: O(1)
    - push_back: O(1)
    - insert_at: O(n)
    - pop_front: O(1)
    - pop_back: O(1)
    - pop_by_data: O(n)
    - pop_by_pos: O(n)
    - size: O(1)
    - reverse: O(n)
    - display: O(n)
*/
class LinkedList
{
    Node* head;
    Node* tail;
    int currentSize{};

    public:
        LinkedList() { head = NULL; }
        ~LinkedList();

        int get_pos(int d);
        int get_data(int pos);

        void push_front(int d);
        void push_back(int d);
        void insert_at(int d, int pos);

        void pop_front();
        void pop_back();
        void pop_by_data(int d);
        void pop_by_pos(int pos);

        int size();
        void reverse();
        void display(bool printReverse = 0);
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
int LinkedList::get_pos(int d)
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
int LinkedList::get_data(int pos)
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
void LinkedList::push_back(int data)
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
void LinkedList::push_front(int data)
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
void LinkedList::insert_at(int data, int pos)
{
    if (pos == 0) push_front(data); 
    else if (pos == currentSize) push_back(data);
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
void LinkedList::pop_front()
{
    if (!head) return;

    Node* temp = head;
    head = head->next;
    head->prev = NULL;
    delete temp;

    currentSize--;
}

// function to delete the node at the back, aka the last node on the right
void LinkedList::pop_back()
{
    if (!head) return;

    Node* temp = tail;
    tail = tail->prev;
    tail->next = NULL;
    delete temp;

    currentSize--;
}

// function to delete a node from the linked list by searching for the specified node with passed in data argument
void LinkedList::pop_by_data(int data)
{
    if (!head) return;

    Node* temp = head;
    while (temp != NULL) {
        if (temp->data == data) {
            if (temp == head) pop_front();
            else if (temp == tail) pop_back();
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
void LinkedList::pop_by_pos(int index)
{
    if (!head) return;

    Node* temp = head;
    int count{};

    while (count < index) {
        temp = temp->next;
        count++;
    }

    if (temp == head) pop_front();
    else if (temp == tail) pop_back();
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
void LinkedList::reverse()
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
void LinkedList::display(bool printReverse)
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

// print a new line
void nl()
{
    std::cout << "\n";
}

void demo()
{
    // initialise a linked list
    std::cout << "Creating a linked list with 5 elements:\n";
    LinkedList list;
    list.push_back(10);
    list.push_back(20);
    list.push_back(30);
    list.push_back(40);
    list.push_back(50);
    list.display();
    std::cout << "Size of linked list: " << list.size() << "\n";

    // searching
    nl();
    std::cout << "Searching for node position with data = 30: " << list.get_pos(30) << "\n";
    std::cout << "Searching for node data with position = 2: " << list.get_data(2) << "\n";

    // reversing linked list
    nl();
    std::cout << "Reversing the linked list:\n";
    list.reverse();
    list.display();

    // insertion
    nl();
    std::cout << "Inserting a new element, 60, at the back of the list:\n";
    list.push_back(60);
    list.display();

    nl();
    std::cout << "Inserting a new element, 70, at the front of the list:\n";
    list.push_front(70);
    list.display();

    nl();
    std::cout << "Inserting a new element, 80, at the position 1 of the list:\n";
    list.insert_at(80, 1);
    list.display();

    // deletion
    nl();
    std::cout << "Deleting the first element of the list:\n";
    list.pop_front();
    list.display();

    nl();
    std::cout << "Deleting the last element of the list:\n";
    list.pop_back();
    list.display();

    nl();
    std::cout << "Deleting the node with data = 40 from the list:\n";
    list.pop_by_data(40);
    list.display();

    nl();
    std::cout << "Deleting the element at the position 1 of the list:\n";
    list.pop_by_pos(1);
    list.display();
}

int main()
{
    std::cout << "Demonstrating Doubly Linked List Implementation:\n\n";
    demo();
    std::cout << "\nEnd of program...";
    return 0;
}