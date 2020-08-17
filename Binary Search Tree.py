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


t = BinarySearchTree()
for x in [10, 1, 2, 3, 6, 4, 9]:
    t.insert(x)
t.inorder()
t.preorder()
t.postorder()
n = t.search(5)
print(n)
