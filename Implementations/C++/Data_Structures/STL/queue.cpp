#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

// print a new line
void nl()
{
    std::cout << "\n";
}

void printQueue(std::queue<int> q, std::string addMsg = "Queue Elements: ")
{
    std::cout << addMsg;
    while (!q.empty()) {
        std::cout << q.front() << " ";
        q.pop(); // pop here since the queue is a FIFO data structure, i.e. accessible after dequeing the front element
    }
    nl();
}

/*
    Queue is a data structure that is a FIFO (First In, First Out) data structure.
    It is a container adaptor, which provides a different interface for accessing its elements.

    The elements are stored in a first-in-first-out (FIFO) order, meaning that the first element added to the queue is the first one to be removed.
    Think of it as a normal queue in real life where the first person to queue up in a restaurant will be the first to be served and leave the queue.

    Functions Time Complexities:
    - push: O(1)
    - pop: O(1)
    - front: O(1)
    - back: O(1)
    - size: O(1)
    - empty: O(1)

    Note: This function will provide a demonstration of the queue data structure using C++ STL (Standard Template Library).
*/
void queue()
{
    std::cout << "Queue Demo\n\n";
    std::queue<int> q;
    // .push() to add enqueue data to the queue
    q.push(10);
    q.push(20);
    q.push(30);
    q.push(40);

    printQueue(q);
    nl();

    // .front() to get the first element of the queue
    std::cout << "Front: " << q.front() << "\n";
    // .back() to get the last element of the queue
    std::cout << "Back: " << q.back() << "\n";
    // .pop() to remove the first element of the queue
    q.pop();
    printQueue(q, "After pop/dequeue: ");
    q.push(10);
    printQueue(q, "After pushing/enqueuing the number 10: ");
    nl();

    // .empty() to check if the queue is empty
    std::cout << "Empty condition: " << (q.empty() ? "True" : "False") << "\n";
    // .size() to get the size of the queue
    std::cout << "Size: " << q.size() << "\n";
    nl();

    // to clear the queue efficiently
    std::queue<int> empty;
    std::swap(q, empty);
    std::cout << "Empty condition after clearing via swapping with empty queue: " << (q.empty() ? "True" : "False") << "\n";
    nl();
    
    // .swap() to swap the queue
    std::cout << "Before swapping:\n";
    std::queue<int> q1;
    q1.push(10);
    q1.push(20);
    q1.push(30);
    printQueue(q1, "Queue One's Elements: ");

    std::queue<int> q2;
    q2.push(40);
    q2.push(50);
    q2.push(60);
    printQueue(q2, "Queue Two's Elements: ");

    nl();
    std::cout << "After swapping:\n";
    q1.swap(q2);
    printQueue(q1, "Queue One's ");
    printQueue(q2, "Queue Two's ");
}

int main()
{
    std::cout << "Demonstrating Queue Implementation using C++ STL:\n\n";
    queue();
    std::cout << "\nEnd of program...";
    return 0;
}