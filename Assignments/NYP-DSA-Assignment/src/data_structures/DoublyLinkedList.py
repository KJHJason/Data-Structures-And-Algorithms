# import standard libraries
from typing import Union

class Node:
    """
    Creates a node object with next and prev pointers
    for the doubly linked list implementation code

    Requires one argument:
    data: the data to be added to the node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    This is a doubly linked list where each nodes are connected together like a chain.
    Each node has a pointer to the previous node and the next node which allows
    bidirectional traversal (i.e. from the head to the tail and from the tail to the head)
    
    Allows for O(1) time complexity for adding and removing nodes 
    from the beginning or the end of the linked list
    
    Additionally, there is no need to shift all elements of the linked list 
    when removing a node unlike a python list/array. Hence, it's faster when 
    removing nodes that are not at the beginning or the end of the linked list.
    
    More details: 
    - https://en.wikipedia.org/wiki/Doubly_linked_list
    - https://www.programiz.com/dsa/doubly-linked-list
    
    References:
    - Introduction to Doubly Linked List
        - https://youtu.be/e9NG_a6Z0mg
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_back(self, data) -> None:
        """
        Add a node to the end of the linked list

        Time Complexity: O(1)

        Requires one argument:
        data: the data to be added to the linked list
        """
        # case 1: if the linked list is empty
        if (self.head is None):
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return

        # case 2: if the linked list has more than one node
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.size += 1

    def remove_node(self, data) -> Union[int, None]:
        """
        Remove a node from the linked list
        
        Best Time Complexity: O(1)
        Worst Time Complexity: O(n)
        Average Time Complexity: O(n)
        
        Advantages over a list:
        - O(1) when removing the node from the beginning or the end of the linkedlist
        - Better performance when removing a node in the linkedlist as it is not necessary to shift the nodes as compared to a list
        
        Requires one argument:
        data: the data to be removed from the linked list
        """
        # case 1: if the linked list is empty
        if (self.head is None):
            return

        # case 2: if the node to be removed is the head
        if (self.head.data == data):
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        # case 3: if the node to be removed is the tail
        if (self.tail.data == data):
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        # case 4: if the linked list has multiple nodes
        current = self.head.next
        while (current is not None):
            # check if the node to be removed is the current node
            if (current.data == data):
                current.prev.next = current.next # if so, set the previous node's next to the current node's next
                current.next.prev = current.prev # set the next node's previous to the current node's previous
                self.size -= 1
                return

            # move to the next node
            current = current.next

        return -1 # return -1 if the node is not in the linked list

    def is_empty(self) -> bool:
        """
        Returns True if the linked list is empty, False otherwise
        """
        return self.size == 0

    def print_list(self) -> None:
        """
        Print the linked list object
        """
        current = self.head
        while (current is not None):
            print(current.data)
            current = current.next

    def convert_to_array(self) -> list:
        """
        Convert the linked list to an array/list
        """
        listOfNodes = []
        current = self.head
        while (current is not None):
            listOfNodes.append(current.data)
            current = current.next
        return listOfNodes

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if (self.head is None):
            return "- []"

        arr = self.convert_to_array()
        arr = [repr(i) for i in arr]
        return f"- [{', '.join(arr)}]"

# test codes for doubly linked list
if (__name__ == "__main__"):
    ll = DoublyLinkedList()
    for i in range(10):
        ll.add_to_back(i)

    print("Original linked list:\n", ll)
    ll.remove_node(8)
    print("\nAfter removing element, \"8\":\n", ll)

    ll.remove_node(0)
    print("\nAfter removing element, \"0\":\n", ll)

    ll.remove_node(9)
    print("\nAfter removing element, \"9\":\n", ll)

    ll.add_to_back(9)
    print("\nAfter adding element, \"9\" to the back:\n", ll)

    print("\nConvert to a python list:\n", ll.convert_to_array())