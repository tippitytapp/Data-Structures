"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BSTNode:
    def __init__(self):
        self.root = None

    # Insert the given value into the tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print('Value is already present in tree')

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.root:
            is_found = self._contains(target, self.root)
            if is_found:
                return True
            return False
        else:
            return None


    def _contains(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._contains(data, cur_node.right)
        elif data< cur_node.data and cur_node.left:
            return self._contains(data, cur_node.left)
        elif data == cur_node.data:
            return True
        


    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, traversal_type):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, start, traversal):
        pass


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
