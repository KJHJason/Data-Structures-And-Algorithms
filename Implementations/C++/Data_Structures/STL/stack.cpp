#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>

// print a new line
void nl()
{
    std::cout << "\n";
}

void printStack(std::stack<int> q, std::string addMsg = "Stack Elements (from top to bottom): ")
{
    std::cout << addMsg;
    while (!q.empty()) {
        std::cout << q.top() << " ";
        q.pop(); // pop here since the stack is a LIFO data structure, i.e. accessible after dequeing the top element
    }
    nl();
}

/*
    Stack is a data structure that is a LIFO (Last In, First Out) data structure.
    It is a container adaptor, which provides a different interface for accessing its elements.

    The elements are stored in a last-in-first-out (LIFO) order, meaning that the last element added to the stack is the first one to be removed.
    Think of it as a stack of plates to be cleaned. It's efficient to put a new plate on the top of the stack of plates to be cleaned. However, it's inefficient to take the plate from the bottom, so we will take the plate from the top to wash it. Hence, the LIFO order.

    Functions Time Complexities:
    - push: O(1)
    - pop: O(1)
    - top: O(1)
    - size: O(1)
    - empty: O(1)

    Note: This function will provide a demonstration of the stack data structure using C++ STL (Standard Template Library).
*/
void stack()
{
    std::stack<int> s;

    // .push() to add enqueue data to the stack
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    printStack(s);
    nl();

    // .top() to get the top element of the stack
    std::cout << "Top: " << s.top();
    nl();

    // .pop() to remove the top element of the stack
    s.pop();
    printStack(s, "After pop (from top to bottom): ");

    // .push() to add enqueue data to the stack
    int n{60}; s.push(n);
    printStack(s, "After pushing the number " + std::to_string(n) + " (from top to bottom): ");
    nl();

    // .size() to get the size of the stack
    std::cout << "Size: " << s.size() << "\n";
    // .empty() to check if the stack is empty
    std::cout << "Empty condition: " << (s.empty() ? "True" : "False") << "\n";
    nl();

    // pop all elements in stack
    std::cout << "After popping all elements from the stack (from top to bottom):\n";
    while (!s.empty()) {
        s.pop();
    }
    printStack(s);

    // .empty() to check if the stack is empty
    std::cout << "Empty condition: " << (s.empty() ? "True" : "False") << "\n";
}

int main()
{
    std::cout << "Demonstrating Stack Implementation using C++ STL:\n\n";
    stack();
    std::cout << "\nEnd of program...";
    return 0;
}