# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 06:13:15 2020

@author: rahul
"""

from random import randint

K=2**32-1
class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        self.priority = randint(0, K)


class Treap:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            from random import shuffle
            temp = [x for x in arr]
            shuffle(temp)
            for x in temp:
                self.insert(x)

    def left_rotate(self, x):
        y = x.right
        b = y.left
        x.right = b

        if b:
            b.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        b = x.right

        y.left = b
        if b:
            b.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

   

    def insert(self, item):
        def insertUtil(node, item):
            if item < node.data:
                if node.left:
                    insertUtil(node.left, item)
                    if node.left.priority>node.priority:
                        self.right_rotate(node)
                else:
                    new_node = Node(item)
                    node.left = new_node
                    new_node.parent = node
                    return new_node
            elif item > node.data:
                if node.right:
                    insertUtil(node.right, item)
                    if node.right.priority>node.priority:
                        self.left_rotate(node)
                else:
                    new_node = Node(item)
                    node.right = new_node
                    new_node.parent = node
                    return new_node
        if self.root is None:
            self.root = Node(item)
            return
        
        node = insertUtil(self.root, item)


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
        
        if target.parent and target.parent.left and target.parent.right:
            if target.parent.left.priority<target.parent.right.priority:
                self.left_rotate(target.parent)
            else:
                self.right_rotate(target.parent)
        
        if target.parent:
            if target.parent.left == target:
                target.parent.left = None
            else:
                target.parent.right = None
            #target.parent = None
        elif target == self.root:
            self.root = None
        target.parent=None

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
        def maxDepth(node):
            if node is None:
                return 0
            ldepth=maxDepth(node.left)
            rdepth=maxDepth(node.right)
            if ldepth>rdepth:
                return ldepth+1
            else:
                return rdepth+1
        return maxDepth(self.root)
        



import time
t = Treap()
s=time.time()
for x in range(2**15):
    t.insert(x)
e=time.time()
print(e-s)
#t.preorder()
s=time.time()
print(t.height())
for x in range(2**15):
    t.delete(x)
e=time.time()
print(e-s)
    

