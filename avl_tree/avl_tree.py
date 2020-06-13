"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, *args):
        self.node = None
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def height(self):
        if self.node:
            return self.node.height
        else: 
            return 0

    def is_leaf(self):
        return self.height == 0

    def update_height(self, recurse = True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_height()
                if self.node.right != None:
                    self.node.right.update_height()
            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height -1

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        pass

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        pass

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height(False)
        self.update_balance(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                self.right_rotate()
                self.update_height()
                self.update_balance()
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()
                self.left_rotate()
                self.update_height()
                self.update_balance()

        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        tree = self.node

        newnode = Node(key)
        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < key.tree:
            self.node.left.insert(key)
        elif key > tree.key:
            self.node.right.insert(key)
        self.rebalance()
