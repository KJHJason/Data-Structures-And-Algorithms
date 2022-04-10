#include <iostream>
#include <vector>
#include <string>

/* ================================= STACK IMPLEMENTATION CODES ================================= */

/*
    Stack is a data structure that is a LIFO (Last In, First Out) data structure.
    It is a container adaptor, which provides a different interface for accessing its elements.

    The elements are stored in a last-in-first-out (LIFO) order, meaning that the last element added to the stack is the first one to be removed.
    Think of it as a stack of plates to be cleaned. It's efficient to put a new plate on the top of the stack of plates to be cleaned. However, it's inefficient to take the plate from the bottom, so we will take the plate from the top to wash it. Hence, the LIFO order.

    Pushing and popping are O(1) operations while searching is an O(n) operation where n is the number of elements in the stack.

    Note: This function will vector for a dynamic array size instead of C array.
*/
class Stack {
    std::vector<int> arr;
    int currentSize{};
    int maxCapacity{};

    public:
        Stack(int maxCap = 0);
        void push(int x);
        void pop();

        int peek();
        int size();

        bool isEmpty();
        bool isFull();

        void clearStack();
        void printStack();
};

// constructor function
Stack::Stack(int maxCap) {
    if (maxCap > 0) maxCapacity = maxCap;
    else if (maxCap < 0) std::cout << "Warning: Max capacity cannot be negative and will be defaulted to unlimited!\n";
}

void Stack::push(int x)
{
    if (isFull()) {
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
    if (isEmpty()) {
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
    if (isEmpty()) {
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

bool Stack::isFull()
{
    if (maxCapacity != 0) return (size() == maxCapacity);
    return 0;
}

bool Stack::isEmpty()
{
    return (size() == 0);
}

void Stack::clearStack()
{
    arr.clear();
    currentSize = 0;
}

void Stack::printStack()
{
    if (isEmpty()) {
        std::cout << "Unable to print: Stack is empty\n";
        return;
    }

    std::cout << "Stack contains (from top to bottom): ";
    for (int i = currentSize - 1; i >= 0; i--) {
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
}

/* ================================= END OF STACK IMPLEMENTATION CODES ================================= */

void br()
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
    s.printStack();

    // .top() to get the top element of the stack
    std::cout << "Top: " << s.peek();
    br();

    // .pop() to remove the top element of the stack
    br();
    s.pop();
    std::cout << "After popping the top element from the stack:\n";
    s.printStack();

    // .push() to add enqueue data to the stack
    br();
    int n{60}; s.push(n);
    std::cout << "After pushing the number " << std::to_string(n) << " (from top to bottom): \n";
    s.printStack();
    br();

    // .size() to get the size of the stack
    std::cout << "Size: " << s.size() << "\n";
    // .empty() to check if the stack is empty
    std::cout << "Empty condition: " << (s.isEmpty() ? "True" : "False") << "\n";
    br();

    // pop all elements in stack
    std::cout << "After clearing the stack:\n";
    s.clearStack();
    s.printStack();

    // .empty() to check if the stack is empty
    std::cout << "Empty condition: " << (s.isEmpty() ? "True" : "False") << "\n";
}

void demoTwo()
{
    // create a stack with max capacity of 5
    Stack s(5);

    // .push() to add enqueue data to the stack
    std::cout << "Creating a stack with max capacity of 5:\n";
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.push(50);
    s.printStack();

    // will print an error when you try to enqueue when the stack is full
    std::cout << "\nPushing the number 60...\n";
    s.push(60);
    std::cout << "As expected, an error message has been printed as the stack is full!\n";
}

int main()
{
    std::cout << "Demonstrating Stack Implementation:\n\n";
    demoOne();
    br();
    demoTwo();
    std::cout << "\nEnd of program...";
    return 0;
}