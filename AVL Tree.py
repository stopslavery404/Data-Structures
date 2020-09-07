# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 06:13:15 2020

@author: rahul
"""


class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        self.height = 1


class AVLTree:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            from random import shuffle
            temp = [x for x in arr]
            shuffle(temp)
            for x in temp:
                self.insert(x)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def left_rotate(self, x):
        y = x.right
        b = y.left

        if b != None:
            b.parent = x
        x.right = b
        y.left = x
        if x.parent and x.parent.left == x:
            x.parent.left = y
        elif x.parent and x.parent.right == x:
            x.parent.right = y
        y.parent = x.parent
        x.parent = y

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def right_rotate(self, x):
        y = x.left
        b = y.right

        if b:
            b.parent = x
        x.left = b
        y.right = x
        if x.parent:
            if x.parent.right == x:
                x.parent.right = y
            else:
                x.parent.left = y
        y.parent = x.parent
        x.parent = y

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, item):
        def insertUtil(root, item):
            if not root:
                return Node(item)
            elif item < root.data:
                root.left = insertUtil(root.left, item)
                root.left.parent = root
            elif item > root.data:
                root.right = insertUtil(root.right, item)
                root.right.parent = root

            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

            balance = self.getBalance(root)
            if balance > 1 and item < root.left.data:
                return self.right_rotate(root)
            elif balance > 1 and item >= root.left.data:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            elif balance < -1:
                if item > root.right.data:
                    return self.left_rotate(root)
                else:
                    root.right = self.right_rotate(root.right)
                    self.left_rotate(root)
            return root

        self.root = insertUtil(self.root, item)

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

    def subtree_minimum(self, node):
        while node.left:
            node = node.left
        return node

    def subtree_maximum(self, node):
        while node.right:
            node = node.right
        return node

    def inorderSuccessor(self, node):
        if not node:
            return
        if node.right:
            return self.subtree_minimum(node.right)
        else:
            current_node = node
            while current_node.parent and current_node.parent.left != current_node:
                current_node = current_node.parent
            if current_node.parent:
                return current_node.parent

    def inorderPredecessor(self, node):
        if not node:
            return
        if node.left:
            return self.subtree_maximum(node.left)
        else:
            current_node = node
            while current_node.parent and current_node.parent.right != current_node:
                current_node = current_node.parent
            if current_node.parent:
                return current_node.parent

    def predecessor(self, key):
        if key < self.min():
            return None
        prev = None
        curr = self.root
        while curr and curr.data != key:
            prev = curr
            if key < curr.data:
                curr = curr.left
            elif key > curr.data:
                curr = curr.right
            else:
                break
        if curr:
            if curr.left:
                return self.subtree_maximum(curr.left)
            else:
                return self.inorderPredecessor(curr)
        elif prev.data < key:
            return prev
        return self.inorderPredecessor(prev)

    def successor(self, key):
        if key > self.max():
            return None
        prev = None
        curr = self.root
        while curr and curr.data != key:
            prev = curr
            if key < curr.data:
                curr = curr.left
            elif key > curr.data:
                curr = curr.right
            else:
                break
        if curr:
            if curr.right:
                return self.subtree_minimum(curr.right)
            else:
                return self.inorderSuccessor(curr)
        elif prev.data > key:
            return prev
        return self.inorderSuccessor(prev)

    def delete(self, item):
        def deleteUtil(root, item):
            if not root:
                return root
            elif item < root.data:
                root.left = deleteUtil(root.left, item)
                if root.left:
                    root.left.parent = root
            elif item > root.data:
                root.right = deleteUtil(root.right, item)
                if root.right:
                    root.right.parent = root
            else:
                if root.left is None:
                    temp = root.right
                    if temp:
                        temp.parent = None
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    if temp:
                        temp.parent = None
                    root = None
                    return temp
                temp = self.subtree_minimum(root.right)
                root.data = temp.data
                root.right = deleteUtil(root.right, temp.data)
                if root.right:
                    root.right.parent = root
            if root is None:
                return root
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            balance = self.getBalance(root)
            if balance > 1:
                if self.getBalance(root.left) >= 0:
                    return self.right_rotate(root)
                else:
                    root.left = self.left_rotate(root.left)
                    if root.left:
                        root.left.parent = root
                    return self.right_rotate(root)
            if balance < -1:
                if self.getBalance(root.right) <= 0:
                    return self.left_rotate(root)
                else:
                    root.right = self.right_rotate(root.right)
                    if root.right:
                        root.right.parent = root
                    return self.left_rotate(root)
            return root

        self.root = deleteUtil(self.root, item)

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

    class Iterator:
        def __init__(self, root):
            self.node = root
            self.stack = []

        def __next__(self):
            if self.node is None and not self.stack:
                raise StopIteration
            while self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            self.node = self.stack.pop()
            item = self.node.data
            self.node = self.node.right
            return item

    def __iter__(self):
        return self.Iterator(self.root)

    def height(self):
        return self.getHeight(self.root)


import time

t = AVLTree()
s = time.time()
for x in range(2 ** 20):
    t.insert(x)
print('height of tree after 1Million insertions', t.height())

e = time.time()
print('time taken for 1Million insertions', e - s)

s = time.time()
for x in range(2 ** 20):
    t.search(x)
e = time.time()
print('time taken for 1Million searches', e - s)

s = time.time()
for x in range(2 ** 20):
    t.delete(x)
e = time.time()
print('time taken for 1Million deletions', e - s)
print(t.height())
