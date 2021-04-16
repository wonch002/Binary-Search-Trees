#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Binary tree implementation.

This python module will serve as a personal implementation of binary trees and
their common algorithms.
"""
__author__ = "Cameron Wonchoba"
__credits__ = ["Cameron Wonchoba"]
__version__ = "0.0.1"
__maintainer__ = "Cameron Wonchoba"
__email__ = "wonch002@umn.edu"
__status__ = "Practice"


class Node:
    """Node class to define a node.

    A node is an object that has a has a left and right child. Using this,
    methods can be written to access different elements of these nodes in a
    strategic way.
    """

    def __init__(self, data):
        """Initialize node.

        Parameters
        ----------
        data : int
            Describes the data that this node should hold
        """
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        """Print binary tree to screen.

        This method will use Inorder Traversal to do this. Luckily,
        we have already implemented this method.
        """
        self.inorder_traversal()

    def insert(self, data):
        """Insert number into binary tree.

        This method will insert a number into a binary tree. The logic will
        follow the convention of typical binary trees:
            - Right node is larger
            - Left node is smaller

        Parameters
        ----------
        data : int
            Number to insert into binary tree
        """
        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def search(self, key):
        """Search for item in tree.

        Returns True if key is present and False if key is not present.

        Parameters
        ----------
        key : int
            item to search for in our BST
        """
        # Base case
        if key == self.data:
            return True

        # Search left if our key is smaller than node
        if key < self.data and self.left is not None:
            return self.left.search(key)

        # Search right if our key is bigger than node
        elif self.right is not None:
            return self.right.search(key)

        # If nothing is found return False
        return False

    def invert(self):
        """Invert binary tree.

        This method will invert a binary tree in place using recursion. This
        works because each node consists of smaller trees that can be inverted
        using the methods (swap left and right nodes).
        """
        temp_left = self.left
        self.left = self.right
        self.right = temp_left

        if self.left is not None:
            self.left.invert()
        if self.right is not None:
            self.right.invert()

    def breadth_first_traversal(self):
        """Print binary tree to screen using breadth first traversal.

        This technique will expand the highest node levels before moving onto
        the next level of nodes.
        """
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)  # Removes first item
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            print(node.data)

    def inorder_traversal(self):
        """Print binary tree to screen using Inorder Traversal.

        This technique will expand the deepest layer nodes first before moving
        onto the higher level nodes. Once we get to a node, we will print it,
        so we don't have to back track. Note, this is the same method we use
        to print our tree, as it prints our data elements in order.

        The basic logic here is:
            - Traverse Left Node
            - Print Node
            - Traverse Right Node
        """
        if self.left:
            self.left.inorder_traversal()

        print(self.data)

        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        """Print binary tree to screen using Preorder Travesal.

        This technique will print nodes to the screen as we reach them. Once a
        node is printed to the screen, the left and right nodes will be
        recursively expanded.

        The basic logic here is:
            - Print Node
            - Traverse Left Node
            - Traverse Right Node
        """
        print(self.data)

        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        """Print binary tree to screen using Postorder Travesal.

        This method will print out the nodes at the deepest layer first. This
        method will also expand an entire sub-tree and all of its deepest
        layers before moving up.

        The basic logic here is:
            - Traverse Left Node
            - Traverse Right Node
            - Print Node
        """
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()

        print(self.data)


def initialize_bst_tree():
    """Initialize a BST tree."""
    root_node = Node(3)
    root_node.insert(12)
    root_node.insert(1)
    root_node.insert(-12)
    root_node.insert(2)
    root_node.insert(5)
    root_node.insert(4)
    root_node.insert(6)

    return root_node


if __name__ == '__main__':
    # Test out tree methods
    root_node = initialize_bst_tree()
    print("Original Tree:")
    root_node.print_tree()
    print()

    print("Inverted Tree:")
    root_node.invert()
    root_node.print_tree()
    print()
    root_node.invert()  # Invert back to get original tree

    print("Breadth First Traversal:")
    root_node.breadth_first_traversal()
    print()

    print("Inorder Traversal:")
    root_node.inorder_traversal()
    print()

    print("Preorder Traversal:")
    root_node.preorder_traversal()
    print()

    print("Postorder Traversal:")
    root_node.postorder_traversal()
    print()
