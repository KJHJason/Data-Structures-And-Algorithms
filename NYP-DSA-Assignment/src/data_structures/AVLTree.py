# import local python files
if (__package__ is None or __package__ == ""):
    from AVLTree_utility_functions import search_node, insert_node, delete_node, inorder_return_node
else:
    from .AVLTree_utility_functions import search_node, insert_node, delete_node, inorder_return_node

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

        # convert the list of linkedlist nodes into a list of RecordData objects
        sortedArr = []
        for node in arr:
            # get the data from the linkedlist and append it to sortedArr
            for data in node.data.convert_to_array():
                sortedArr.append(data)

        # return the sorted list of RecordData objects by customer name
        return sortedArr

    def move_node(self, data) -> None:
        """
        Used when the user has changed the customer name in one of the nodes in the tree.
        Hence, there will be a need to delete the old data in the linkedlist that may result 
        in deletion of the tree node if there is only one data in the linkedlist.
        Since, there is a new customer name, we will have to insert a node into the root with a new key.
        
        Requires one argument:
        - data (RecordData): The data of the node to be deleted from the linkedlist
        """
        self.delete(data)
        self.insert(data)

    def search(self, target:str):
        return search_node(self.root, target)

    def insert(self, data) -> None:
        self.root = insert_node(self.root, data)

    def delete(self, data) -> None:
        self.root = delete_node(self.root, data)

    def visualise_tree(self, root, indent:str="", rightChildNode:bool=True) -> None:
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

# demo codes below (with some explanations)
if (__name__ == "__main__"):
    from uuid import uuid4
    import timeit, random
    class TestData:
        def __init__(self, name):
            self.__customer_name = name
            self.id = uuid4().hex

        def get_customer_name(self):
            return self.__customer_name

        def __repr__(self):
            return f"{self.__customer_name} ({self.id})"

    nodeList = []
    for i in range(0, 20, 4):
        for j in range(3):
            # nodeList.append(TestData(f"Customer {i}"))
            nodeList.append(TestData(i)) # using numbers instead of strings for easier understanding

    tree = AVLTree()
    for node in nodeList:
        tree.insert(node)

    print("Original tree:")
    print(tree)

    print("\nsearching...")
    print("Result:\n", tree.search(nodeList[0].get_customer_name()))

    # doesn't delete any nodes from the tree but removes
    # a node from the doubly linked list that stores data of the same key.
    tree.delete(nodeList[0])
    print("\ntree after deleting one data from the node:")
    print(tree)

    # After deleting the tree node, 0
    #  4 (bf = -2)
    #   \
    #   12
    #  / \
    # 8  16
    # tree becomes unbalanced (right heavy) and 
    # requires rotations (right right case) to balance it.
    # It will do a simple left rotation on node 4 which is the root
    # After the rotation, the tree is balanced again with node 12 as the new root.
    for i in range(1, 3):
        tree.delete(nodeList[i])
    print("\ntree after deleting the tree node 0:")
    print(tree)

    # When the customer 8 tree node is deleted from the AVL Tree
    # No rebalancing is required.
    for i in range(6, 9):
        tree.delete(nodeList[i])
    print("\ntree after deleting the tree node 8:")
    print(tree)

    print("\nTree sort by int:")
    arr = tree.tree_sort()
    [print(repr(x)) for x in arr]

    del tree # explicitly delete for garbage collection

    # demo for the time complexity of the tree sort
    while (1):
        print("\nWill start a demo of tree sort on 1 million elements in an array...")
        print("This will take a while and ensure you have around 0.6GB+ of free memory...")
        confirmInput = input("Continue? (y/n): ").lower()
        if (confirmInput == "y"):
            # demo the time taken to sort the tree
            print("\nTree sort with 1 million elements in an array...")
            arr = [TestData(random.randint(0, 1000000)) for _ in range(1000000)]

            def test_tree_sort(arr):
                newTree = AVLTree()
                for el in arr:
                    newTree.insert(el)
                sortedArr = newTree.tree_sort()

                # assert that the sorted array is sorted correctly
                assert sortedArr == sorted(arr, key=lambda x: x.get_customer_name())

            print("Time taken:", timeit.timeit(lambda: test_tree_sort(arr), number=1))
            break
        elif (confirmInput == "n"):
            print("Aborting...")
            break
        else:
            print("Invalid input. Try again.")
            continue