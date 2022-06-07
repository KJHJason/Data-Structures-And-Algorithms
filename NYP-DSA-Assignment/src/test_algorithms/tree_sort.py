from typing import Union

class TreeNode:
    """
    Creates a TreeNode object with the given data

    Requires one argument:
    data: the data to be added to the node
    
    Will create a doubly linked list to store all occurrences of the key (customer name)
    to prevent duplicate keys in the BST.
    """
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
        self.height = 1 # Initialise height to 1 since a node has a height of 1 by itself
        self.data = DoublyLinkedList() # to store data of the same customer name

        self.data.add_to_back(data)

class Node:
    """
    Creates a node object with next and prev pointers
    for the doubly linked list implementation code

    Requires one argument:
    data: the data to be added to the node
    """
    def __init__(self, data:int):
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

    def add_to_back(self, data:int) -> None:
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

    def remove_node(self, data:int) -> Union[int, None]:
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

class AVLTree:
    """
    This is an AVL tree that is a type of self-balancing binary search tree where
    the heights of the left and right subtrees of any node differ by less than or equal to 1.
    Each node has a balance factor of -1, 0, or 1. Otherwise, the tree is not balanced which will
    result in rotations in an effort to balance the tree.
    
    The balancing of the tree help to guarantee that insertion, deletion, 
    and search are O(log n) operations.
    
    References:
    - https://en.wikipedia.org/wiki/AVL_tree
    - https://www.javatpoint.com/avl-tree
    - https://favtutor.com/blogs/avl-tree-python
    - AVL Trees & Rotations (Self-Balancing Binary Search Trees)
        - https://www.youtube.com/watch?v=vRwi_UcZGjU&feature=youtu.be

    Explanations and Python implementation:
        - https://www.programiz.com/dsa/avl-tree
        - AVL Tree: Background & Python Code
            - https://www.youtube.com/watch?v=lxHF-mVdwK8&feature=youtu.be
    
    Useful websites that visualises the AVL tree rotations:
    - https://www.cs.usfca.edu/%7Egalles/visualization/AVLtree.html
    - https://visualgo.net/en/bst?mode=AVL
    """
    def __init__(self):
        self.root = None

    def insert_array(self, arr:list[int]) -> None:
        """
        Insert an array of integers into the AVL tree
        """
        for el in arr:
            self.insert(el)

    def tree_sort(self, reverse:bool=False) -> list:
        """
        Returns a sorted array of the tree by customer name
        
        Best Time complexity: O(n)
        Worst Time complexity: O(n)
        Average Time complexity: O(n)
        
        Note: It is O(n) in this case as in the HotelDatabase object, the AVLTree object is automatically
        updated every time the user adds, changes, or deletes a customer name.
        Hence, removing the need to insert the nodes into the tree when sorting using tree sort.
        
        Space complexity: O(m + n)
        Where m is the number of nodes in the tree (stored in arr) and 
        n is the number of elements (inside all linkedlist) in the tree (stored in sortedArr)
        
        Requires one argument:
        - reverse (bool): Whether to return the nodes in ascending or descending order. Defaults to False
        """
        if (self.root is None):
            return []

        arr = []
        inorder_return_node(self.root, arr, reverse=reverse) # will return a list of linkedlist nodes

        # convert the list of linkedlist nodes into a list of integers
        sortedArr = []
        for node in arr:
            # get the data from the linkedlist and append it to sortedArr
            for data in node.data.convert_to_array():
                sortedArr.append(data)

        # return the sorted list of integers
        return sortedArr

    def move_node(self, data:int) -> None:
        """
        Used when the user has changed the customer name in one of the nodes in the tree.
        Hence, there will be a need to delete the old data in the linkedlist that may result 
        in deletion of the tree node if there is only one data in the linkedlist.
        Since, there is a new customer name, we will have to insert a node into the root with a new key.
        
        Requires one argument:
        - data (int): The data of the node to be deleted from the linkedlist
        """
        self.delete(data)
        self.insert(data)

    def search(self, target:int):
        return search_node(self.root, target)

    def insert(self, data:int) -> None:
        self.root = insert_node(self.root, data)

    def delete(self, data:int) -> None:
        self.root = delete_node(self.root, data)

    def visualise_tree(self, root:TreeNode, indent:str="", rightChildNode:bool=True) -> None:
        """
        Print the tree in a visual representation
        in a preorder traversal (Visit, Left, Right)
        
        Requires three arguments:
        root: the root of the tree
        indent: the indentation of the current node
        rightChildNode: the node that is the right child of the current node
        """
        if (root):
            print(indent, end="")
            if (rightChildNode):
                print("R-----", end="")
                indent += "     "
            else:
                print("L-----", end="")
                indent += "|    "

            print(root.key, f"({len(root.data)} elements)")
            self.visualise_tree(root.left, indent, False)
            self.visualise_tree(root.right, indent, True)

    def __str__(self) -> str:
        self.visualise_tree(self.root)
        return ""

def get_height(node:TreeNode) -> int:
    """
    Get the height of the tree from the node
    
    Requires one argument:
    - node (TreeNode): the node to get the height from
    """
    if (node is None):
        return 0

    return node.height

def get_balance(root:TreeNode) -> int:
    """
    Get the balance factor of the tree
    
    Formula:
    get_balance(x) = get_height(left child) - get_height(right child)
    
    Balance factor is used to determine if the tree is balanced or not.
    
    A tree is balanced if the balance factor is -1, 0, or 1
    
    Requires one argument:
    - root (TreeNode): The root node of the tree/subtree
    """
    if (root is None):
        return 0

    return get_height(root.left) - get_height(root.right)

def get_min_value(root:TreeNode) -> TreeNode:
    """
    Find the minimum value node in the tree
    
    Requires one argument:
    - root (TreeNode): The root node of the tree/subtree
    """
    current = root

    # loop down to find the leftmost leaf as the smallest node is 
    # the left child of a root node of a subtree
    while (current.left is not None):
        current = current.left

    return current

def left_rotate(x:TreeNode) -> TreeNode:
    """
    To perform left rotation on the subtree rooted with x
    
    Requires one argument:
    - x (TreeNode): The root node of the subtree
    """
    y = x.right
    childSubtree = y.left
    
    # Perform the rotation
    y.left = x
    x.right = childSubtree

    # update the heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y:TreeNode) -> TreeNode:
    """
    To perform right rotation on the subtree rooted with y
    
    Requires one argument:
    - y (TreeNode): The root node of the subtree
    """
    x = y.left
    childSubtree = x.right
    
    # perform the rotation
    x.right = y
    y.left = childSubtree

    # update the heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def search_node(root:TreeNode, target:int) -> Union[DoublyLinkedList, int]:
    """
    Do a search on the tree
    
    Best Time complexity: O(log n)
    Worst Time complexity: O(log n)
    Average Time complexity: O(log n)

    Requires two arguments:
    - root (TreeNode): The root node of the tree/subtree
    - target (string): The target value to search for (customer name)
    """
    # If the target is less than the current node, search the left subtree
    if (target < root.key):
        if (root.left is None):
            return -1 # If the left child is empty, return -1
        else:
            return search_node(root.left, target)
    # If the target is greater than the current node, search the right subtree
    elif (target > root.key):
        if (root.right is None):
            return -1 # If the right child is empty, return -1
        else:
            return search_node(root.right, target)
    else:
        # If the target is equal to the current node, return 
        # a linkedlist of hotel record objects
        return root.data 

def insert_node(root:TreeNode, data:int) -> TreeNode:
    """
    Insert a node into the tree or append the data to the linkedlist in the node
    
    Best Time complexity: O(log n)
    Worst Time complexity: O(log n)
    Average Time complexity: O(log n)
    
    Requires two arguments:
    - root (TreeNode): The root node of the tree/subtree
    - data (int): The data of the node to be inserted into the tree
    """
    # If the tree is empty, return a new node as the root
    # or if we have reached the child of a leaf node, change the child to 
    # the new node with the data inserted instead of pointing to None
    if (root is None):
        return TreeNode(data)
    # If the data key is less than the current node, insert the node to the left subtree
    elif (data < root.key):
        root.left = insert_node(root.left, data)
    # If the data key is greater than the current node, insert the node to the right subtree
    elif (data > root.key):
        root.right = insert_node(root.right, data)
    # If the data key is equal to the current node, append the data to the linkedlist in the node
    else:
        root.data.add_to_back(data)
        return root

    # update the height of the current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # get the balance factor of the current node to check if the tree needs to be balanced
    balanceFactor = get_balance(root)
    
    # If the balance factor is greater than 1, the tree needs to be balanced
    if (balanceFactor > 1):
        # If the data key is less than the left child, rotate right
        if (data < root.left.key):
            # e.g. of left left case
            #             5 (bf:  2-0 = 2)
            #            /
            #           2 (bf: 1-0 = 1)
            #          /
            # (bf: 0) 1 
            # Afterwards, in this example, we will have to balance the tree with 
            # a right rotation on the subtree with root 5.
            # 
            # y = 5
            # initialise x and childSubtree
            # x = y.left (5.left = 2)
            # childSubtree = x.right (2.right = None)
            # 
            # then we perform the rotation
            # 2.right = y (5)
            # 5.left = childSubtree (None)
            # 
            # return x node (2)
            # 
            # After doing a right rotation (clockwise rotation), the balanced tree will look like this:
            #           2 (bf: 1-1 = 0)
            #          / \
            # (bf: 0) 1   5 (bf: 0)

            return right_rotate(root)
        # If the data key is greater than the right child, rotate left and then rotate right
        else:
            # e.g. of left right case
            # 
            #   5 (bf:  2-0 = 2)
            #  / 
            # 2 (bf: 0-2 = -2)
            #  \
            #   3 (bf: 0-1 = -1)
            # 
            # Afterwards, in this example, we will have to balance the tree with a left rotation 
            # and then a right rotation (left right case).
            # 
            # First left rotation (anti-clockwise rotation) on the 
            # left child of the subtree rooted at node 2:
            #     5 (bf:  2-0 = 2)
            #    / 
            #   3 (bf: 1-0 = 1) 
            #  /
            # 2 (bf: 0
            # 
            # Then right rotation (clockwise rotation) on the subtree rooted at node 5:
            #           3 (bf:  1-1 = 0)
            #          / \
            # (bf: 0) 2   5 (bf: 0)

            root.left = left_rotate(root.left)
            return right_rotate(root)

    # If the balance factor is less than -1, the tree needs to be balanced
    if (balanceFactor < -1):
        # If the data key is greater than the right child, rotate left
        if (data > root.right.key):
            # e.g. of right right case
            # 5 (bf:  0-2 = -2)
            #  \
            #   6 (bf: 0-1 = -1)
            #    \
            #     8 (bf: 0)
            # Afterwards, in this example, we will have to balance the tree with a left rotation
            # on the subtree with root 5.
            # 
            # x = 5
            # initialise y and childSubtree
            # y = x.right (5.right = 6)
            # childSubtree = y.left (6.left = None)
            # 
            # then we perform the rotation
            # 6.left = x (5)
            # 5.right = childSubtree (None)
            # 
            # return y node (6)
            # 
            # After doing a left rotation (anti-clockwise rotation), 
            # the balanced tree will look like this:
            #           6 (bf: 1-1 = 0)
            #          / \
            # (bf: 0) 5   8 (bf: 0)

            return left_rotate(root)
        # If the data key is less than the left child, rotate right and then rotate left
        else:
            # e.g. of right left case
            # 
            # 1 (bf:  0-2 = -2)
            #  \ 
            #   3 (bf: 1-0 = 1)
            #  /
            # 2(bf: 0)
            # 
            # Afterwards, in this example, we will have to balance the tree with a right rotation
            # and then a left rotation (right left case).
            # 
            # First right rotation (clockwise rotation) on the right child of the subtree rooted at node 3:
            # 1 (bf:  0-2 = -2)
            #  \
            #   2 (bf: -1-0 = -1)
            #    \
            #     3 (bf: 0)
            # 
            # Then left rotation (anti-clockwise rotation) on the subtree rooted at node 1:
            #           2 (bf:  1-1 = 0)
            #          / \
            # (bf: 0) 1   3 (bf: 0)

            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def delete_node(root:TreeNode, data:int) -> TreeNode:
    """
    Delete a node from the tree and balance the tree if the node is deleted
    
    Best Time complexity: O(log n)
    Worst Time complexity: O(log n)
    Average Time complexity: O(log n)
    
    Requires two argument:
    - root (TreeNode): The root node of the tree/subtree
    - data (int): The data of the node to be deleted from the linkedlist
    """
    # if the root is None, return None.
    # This will happen if the node to be deleted is not in the tree
    if (root is None):
        return root
    # If the target is smaller than the current node, search the left subtree
    elif (data < root.key):
        root.left = delete_node(root.left, data)
    # If the target is greater than the current node, search the right subtree
    elif (data > root.key):
        root.right = delete_node(root.right, data)
    # target found!
    else:
        # if the node has more than one object inside the linkedlist, delete the target object from the linkedlist
        if (len(root.data) > 1):
            root.data.remove_node(data)
            return root

        # if the node has only one or no child, replace the node with its child or None
        # and delete the node that is to be deleted from the tree
        if (root.left is None):
            temp = root.right
            del root # explicitly delete the node for garbage collection
            return temp
        elif (root.right is None):
            temp = root.left
            del root # explicitly delete the node for garbage collection
            return temp

        # if the node has two childrens, find the inorder successor 
        # (smallest value in the right subtree/
        # the node with the smallest key greater than the key of the input node)
        # 
        # e.g. 
        #                 4 (bf: 2-1 = 1)
        #                / \
        # (bf: 1-1 = 0) 2   5 (bf: 0)
        #              / \
        #    (bf: 0) 1   3 (bf: 0)
        # 
        # If we want to delete the node with value 4, we will find 
        # the inorder successor in the right subtree which will be the node with value 5.
        # 
        #             5 (inorder successor, bf: 2-0 = 2)
        #            /
        #           2 (bf: 1-1 = 0)
        #          / \
        # (bf: 0) 1   3 (bf: 0)
        # 
        # We will then replace the node that we wanted to delete 
        # with the inorder successor as shown above.

        temp = get_min_value(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key
        root.data = temp.data

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)

    # if the tree had only one node, just return it as there is no need to balance the tree
    if (root is None):
        return root

    # Now, to balance the tree...
    # update the height of the current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # get the balance factor of the current node to check if the tree needs to be balanced
    balanceFactor = get_balance(root)
    
    # If the balance factor is greater than 1, the tree needs to be balanced
    if (balanceFactor > 1):
        # If the balance factor of the left child is greater than 1, rotate right
        if (get_balance(root.left) >= 0):
            # Left left case
            return right_rotate(root)
        # If the balance factor of the left child is less than 0, rotate left and then rotate right
        else:
            # Left right case
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # If the balance factor is less than -1, the tree needs to be balanced
    if (balanceFactor < -1):
        # If the balance factor of the right child is less than -1, rotate left
        if (get_balance(root.right) <= 0):
            # Right right case
            return left_rotate(root)
        # If the balance factor of the right child is greater than 0, rotate right and then rotate left
        else:
            # Right left case
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def inorder_return_node(root:TreeNode, arr:list, reverse:bool=False) -> list:
    """
    Traverse the tree in order and return the nodes by appending them to an array
    
    Requires two arguments:
    - arr (list): The array to append the nodes to
    - reverse (bool): Whether to return the nodes in ascending or descending order. 
                      Defaults to False for ascending order.
    """
    if (not root):
        return

    if (reverse):
        inorder_return_node(root.right, arr, reverse)
        arr.append(root)
        inorder_return_node(root.left, arr, reverse)
    else:
        inorder_return_node(root.left, arr, reverse)
        arr.append(root)
        inorder_return_node(root.right, arr, reverse)