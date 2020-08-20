# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 02:51:47 2020

@author: rahul
"""

'''BST with duplicates allowed'''


class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        self.repeat_left = False


class BinarySearchTree:
    '''duplicates allowed'''

    def __init__(self, arr=None):
        self.root = None
        if arr:
            from random import shuffle
            temp = [x for x in arr]
            shuffle(temp)
            for x in temp:
                self.insert(x)

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
            elif item == node.data:
                if node.repeat_left:
                    node.repeat_left = False
                    if node.left:
                        insertUtil(node.left, item)
                    else:
                        new_node = Node(item)
                        node.left = new_node
                        new_node.parent = node
                        return
                else:
                    node.repeat_left = True
                    if node.right:
                        insertUtil(node.right, item)
                    else:
                        new_node = Node(item)
                        node.right = new_node
                        new_node.parent = node
                        return

            else:
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

    def subtree_minimum(self, node):
        while node.left:
            node = node.left
        return node

    def subtree_maximum(self, node):
        while node.right:
            node = node.right
        return node

    def successor(self, node):
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

    def predecessor(self, node):
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

    def delete(self, item):
        target = self.search(item)
        if target is None:
            return
        while target.right:
            successor = self.successor(target)
            target.data, successor.data = successor.data, target.data
            target = successor

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


t = BinarySearchTree()

for x in [17, 3, 2, 6, 8, 5, 18, 1, 14, 13, 7, 4, 9, 11, 10, 16, 19, 20, 12, 15]:
    t.insert(x)
for i in range(2, 21):
    print(i, t.predecessor(t.search(i)).data)
#   print(i, t.delete(i))
#  t.inorder()
