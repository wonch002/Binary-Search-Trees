#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Binary tree implementation.

This python module will serve as a personal implementation of binary trees and
their common algorithms.
"""


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
        """Print binary tree to screen."""
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

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

    def check_leaf(self):
        """Return whether node is a leaf node or not."""
        return self.right is None and self.left is None

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
   
    def breadth_first_search(self):
        """Print binary tree to screen using breadth first search.

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


if __name__ == '__main__':
    # Test out tree
    root_node = Node(3)
    root_node.insert(12)
    root_node.insert(1)
    root_node.insert(-12)
    root_node.insert(2)
    root_node.insert(5)
    root_node.insert(4)
    #root_node.print_tree()
    #root_node.invert()
    #root_node.print_tree()
    #root_node.invert()
    root_node.breadth_first_search()