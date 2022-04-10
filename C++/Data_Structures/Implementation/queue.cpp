#include <iostream>
#include <vector>

/* ================================= QUEUE IMPLEMENTATION CODES ================================= */

/*
    Queue is a data structure that is a FIFO (First In, First Out) data structure.
    It is a container adaptor, which provides a different interface for accessing its elements.

    The elements are stored in a first-in-first-out (FIFO) order, meaning that the first element added to the queue is the first one to be removed.
    Think of it as a normal queue in real life where the first person to queue up in a restaurant will be the first to be served and leave the queue.

    Methods Time Complexities:
    - enqueue: O(1)
    - dequeue: O(1)
    - peek: O(1)
    - size: O(1)
    - isEmpty: O(1)
    - isFull: O(1)

    Note: This function uses vector for a dynamic array size instead of C array. Thus, not needing a front and rear pointer.
*/
class Queue
{
    std::vector<int> arr; // using vector for dynamic size to store the elements instead of C array
    int currentSize{};    // current size of the queue
    int maxCapacity{};    // maximum capacity of the queue          

    public:
        Queue(int s = 0);
    
        void dequeue();
        void enqueue(int x);

        int peek();
        int back();
        int size();
        
        bool isEmpty();
        bool isFull();

        void clearQueue();
        void printQueue();
};

// constructor function
Queue::Queue(int maxCap) {
    if (maxCap > 0) maxCapacity = maxCap;
    else if (maxCap < 0) std::cout << "Warning: Max capacity cannot be negative and will be defaulted to unlimited!\n";
}

// function to dequeue the front element
void Queue::dequeue()
{
    // check for queue underflow
    if (isEmpty()) {
        std::cout << "Error: Queue Underflow\n";
        return;
    }

    // Dequeue the front element
    arr.erase(arr.begin());

    // Update the queue size
    currentSize--;
}

// function to add an item to the queue
void Queue::enqueue(int item)
{
    // check for queue overflow
    if (isFull()) {
        std::cout << "Error: Queue Overflow\n";
        return;
    }

    // Add the item to the queue to the back
    arr.push_back(item);

    // Update the queue size
    currentSize++;
}

// function to return the front element of the queue
int Queue::peek()
{
    if (isEmpty()) {
        std::cout << "Error: Queue is empty!\n";
        return -1;
    }
    return arr.front();
}

int Queue::back()
{
    if (isEmpty()) {
        std::cout << "Error: Queue is empty!\n";
        return -1;
    }
    return arr.back();
}

// function to return the size of the queue
int Queue::size() {
    return currentSize;
}

// function to check if the queue is empty or not
bool Queue::isEmpty() {
    return (size() == 0);
}

// function to check if the queue is full or not
bool Queue::isFull() {
    if (maxCapacity != 0) return (size() == maxCapacity);
    return 0;
}

// function to clear the queue
void Queue::clearQueue()
{
    arr.clear();
    currentSize = 0;
}

// function to display the queue
void Queue::printQueue()
{
    if (isEmpty()) {
        std::cout << "Unable to print: Queue is empty\n";
        return;
    }

    std::cout << "Queue: ";
    for (auto i : arr) {
        std::cout << i << " ";
    }
    std::cout << "\n";
}

/* ============================== END OF QUEUE IMPLEMENTATION CODES ============================== */

void demoOne()
{
    // create a queue with no max capacity limit
    std::cout << "Creating a queue with no max capacity limit:\n";
    Queue q; 

    // add some elements to the queue
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);

    // print the queue
    q.printQueue();

    // .peek() for the front element
    std::cout << "Front: " << q.peek() << "\n";

    // .back() for the back element
    std::cout << "Back: " << q.back() << "\n";

    // .size() to get the size of the queue
    std::cout << "Size: " << q.size() << "\n";

    // .isEmpty() to check if the queue is empty
    std::cout << "Empty condition: " << (q.isEmpty() ? "True" : "False") << "\n";

    // .dequeue() to dequeue the front element
    std::cout << "\nDequeuing the front element, number 10:\n";
    q.dequeue();
    q.printQueue();

    // .enqueue() to add an element to the queue
    std::cout << "\nEnqueuing the number 10 back to the queue:\n";
    q.enqueue(10);
    q.printQueue();
    

    // .clearQueue() to clear the queue
    std::cout << "\nClearing the queue:\n";
    q.clearQueue();
    q.printQueue();
    std::cout << "Empty condition: " << (q.isEmpty() ? "True" : "False") << "\n\n";
}

void demoTwo()
{
    std::cout << "Creating a queue with a max capacity of 5:\n";
    Queue q(5);

    // add some elements to the queue
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);
    q.enqueue(50);

    // print the queue
    q.printQueue();

    // will print an error when you try to enqueue when the queue is full
    std::cout << "\nEnqueuing the number 60...\n";
    q.enqueue(60);
    std::cout << "As expected, an error message has been printed as the queue is full!\n";
}

int main()
{
    std::cout << "Demonstrating Queue Implementation:\n\n";
    demoOne();
    demoTwo();
    std::cout << "\nEnd of program...";
    return 0;
}