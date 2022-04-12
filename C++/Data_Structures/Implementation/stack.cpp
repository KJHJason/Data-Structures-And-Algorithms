#include <iostream>
#include <vector>
#include <string>

/* ================================= STACK IMPLEMENTATION CODES ================================= */

/*
    Stack is a data structure that is a LIFO (Last In, First Out) data structure.
    It is a container adaptor, which provides a different interface for accessing its elements.

    The elements are stored in a last-in-first-out (LIFO) order, meaning that the last element added to the stack is the first one to be removed.
    Think of it as a stack of plates to be cleaned. It's efficient to put a new plate on the top of the stack of plates to be cleaned. However, it's inefficient to take the plate from the bottom, so we will take the plate from the top to wash it. Hence, the LIFO order.

    Methods Time Complexities:
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - size: O(1)
    - is_empty: O(1)
    - is_full: O(1)
    - display: O(n)
    - capacity: O(1)

    Note: This function will vector for a dynamic array size instead of C array.
*/
class Stack {
    std::vector<int> arr;
    int currentSize{};
    int maxCapacity{};

    public:
        Stack(int maxCap = 0);
        ~Stack();

        void push(int x);
        void pop();

        int peek();
        int size();

        bool is_empty();
        bool is_full();

        void display();
        int capacity();
};

// destructor function to clear vector
Stack::~Stack() 
{
    arr.clear();
}

// constructor function to define the max capacity of the queue if given
Stack::Stack(int maxCap) {
    if (maxCap > 0) maxCapacity = maxCap;
    else if (maxCap < 0) std::cout << "Warning: Max capacity cannot be negative and will be defaulted to unlimited!\n";
}

void Stack::push(int x)
{
    if (is_full()) {
        std::cout << "Error: Stack Overflow\n";
        return;
    }

    // push element to the top of the stack
    arr.push_back(x);

    // update size
    currentSize++;
}
void Stack::pop()
{
    if (is_empty()) {
        std::cout << "Error: Stack Underflow";
        return;
    }
    
    // pop element from the top of the stack
    arr.pop_back();

    // update size
    currentSize--;
}

int Stack::peek()
{
    if (is_empty()) {
        std::cout << "Stack is Empty";
        return -1;
    }
    
    // return top element of the stack
    return arr.back();
}

int Stack::size()
{
    return currentSize;
}

bool Stack::is_full()
{
    if (maxCapacity != 0) return (size() == maxCapacity);
    return 0;
}

bool Stack::is_empty()
{
    return (size() == 0);
}

void Stack::display()
{
    if (is_empty()) {
        std::cout << "Unable to print: Stack is empty\n";
        return;
    }

    std::cout << "Stack contains (from top to bottom): ";
    for (int i = currentSize - 1; i >= 0; i--) {
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
}

int Stack::capacity()
{
    return maxCapacity;
}

/* ================================= END OF STACK IMPLEMENTATION CODES ================================= */

// print a new line
void nl()
{
    std::cout << "\n";
}

void demoOne()
{
    // create a stack with no max capacity limit
    Stack s;

    // .push() to add enqueue data to the stack
    std::cout << "Creating a stack with no capacity limit:\n";
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.display();

    // .top() to get the top element of the stack
    std::cout << "Top: " << s.peek();
    nl();

    // .pop() to remove the top element of the stack
    nl();
    s.pop();
    std::cout << "After popping the top element from the stack:\n";
    s.display();

    // .push() to add enqueue data to the stack
    nl();
    int n{60}; s.push(n);
    std::cout << "After pushing the number " << std::to_string(n) << " (from top to bottom): \n";
    s.display();
    nl();

    // .size() to get the size of the stack
    std::cout << "Size: " << s.size() << "\n";
    // .empty() to check if the stack is empty
    std::cout << "Empty condition: " << (s.is_empty() ? "True" : "False") << "\n";
    nl();

    // pop all elements in stack
    std::cout << "After clearing the stack:\n";
    while (!s.is_empty()) {
        s.pop();
    }
    s.display();

    // .empty() to check if the stack is empty
    std::cout << "Empty condition: " << (s.is_empty() ? "True" : "False") << "\n";
}

void demoTwo()
{
    // create a stack with max capacity of 5
    Stack s(5);

    // .push() to add enqueue data to the stack
    std::cout << "Creating a stack with max capacity of ";
    std::cout << s.capacity() << ":\n";
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.push(50);
    s.display();

    // will print an error when you try to enqueue when the stack is full
    std::cout << "\nPushing the number 60...\n";
    s.push(60);
    std::cout << "As expected, an error message has been printed as the stack is full!\n";
}

int main()
{
    std::cout << "Demonstrating Stack Implementation:\n\n";
    demoOne();
    nl();
    demoTwo();
    std::cout << "\nEnd of program...";
    return 0;
}