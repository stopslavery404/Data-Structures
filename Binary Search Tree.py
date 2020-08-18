# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:59:19 2020

@author: rahul
"""


class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
            return

        def insertUtil(node, item):
            if item < node.data:
                if node.left:
                    insertUtil(node.left, item)
                else:
                    new_node = Node(item)
                    node.left = new_node
                    new_node.parent = node
                    return
            elif item > node.data:
                if node.right:
                    insertUtil(node.right, item)
                else:
                    new_node = Node(item)
                    node.right = new_node
                    new_node.parent = node
                    return

        insertUtil(self.root, item)

    def inorder(self):
        node = self.root

        def inorderUtil(node):
            if node:
                if node.left:
                    inorderUtil(node.left)
                print(node.data, end=' ')
                if node.right:
                    inorderUtil(node.right)

        inorderUtil(node)
        print()

    def preorder(self):
        node = self.root

        def preorderUtil(node):
            if node:
                print(node.data, end=' ')
                if node.left:
                    preorderUtil(node.left)
                if node.right:
                    preorderUtil(node.right)

        preorderUtil(node)
        print()

    def postorder(self):
        node = self.root

        def postorderUtil(node):
            if node:
                if node.left:
                    postorderUtil(node.left)
                if node.right:
                    postorderUtil(node.right)
                print(node.data, end=' ')

        postorderUtil(node)
        print()

    def search(self, item):
        def searchUtil(root, item):
            if not root:
                return None
            if root.data == item:
                return root
            if item < root.data:
                return searchUtil(root.left, item)
            if item > root.data:
                return searchUtil(root.right, item)

        return searchUtil(self.root, item)

    def successor(self, node):
        current_node = node.right
        while current_node and current_node.left:
            current_node = current_node.left
        return current_node

    def predecessor(self, node):
        current_node = node.left
        while current_node and current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, item):
        target = self.search(item)
        if target is None:
            return
        successor = self.successor(target)
        while successor:
            target.data, successor.data = successor.data, target.data
            target = successor
            successor = self.successor(target)
        if target.parent:
            if target.parent.left == target:
                target.parent.left = None
            else:
                target.parent.right = None
            target.parent = None
        elif target == self.root:
            self.root = None

    def max(self):
        m = float('-inf')
        node = self.root
        while node and node.right:
            node = node.right
        if node:
            m = max(m, node.data)
        return m

    def min(self):
        m = float('inf')
        node = self.root
        while node and node.left:
            node = node.left
        if node:
            m = min(m, node.data)
        return m

    def path_to_root(self, node):
        arr = []
        arr.append(node.data)
        while node != self.root:
            node = node.parent
            arr.append(node.data)
        print(arr)


t = BinarySearchTree()

for x in [17, 3, 2, 6, 8, 5, 18, 1, 14, 13, 7, 4, 9, 11, 10, 16, 19, 20, 12, 15]:
    t.insert(x)
