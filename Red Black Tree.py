# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:59:19 2020

@author: rahul
"""
from random import shuffle

RED = True
BLACK = False


class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        self.color = BLACK


class RedBlackTree:
    def __init__(self, arr=None):
        self.NIL = Node(None)
        self.root = self.NIL
        self.root.parent = self.NIL
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

        if b != self.NIL:
            b.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
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
        if b != self.NIL:
            b.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, item):
        z = Node(item)
        z.left = self.NIL
        z.right = self.NIL
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = RED
        self.insertFixup(z)

    def insertFixup(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)
        self.root.color = BLACK

    def inorder(self):
        node = self.root

        def inorderUtil(node):
            if node != self.NIL:
                if node.left:
                    inorderUtil(node.left)
                if node.color:
                    color = 'r'
                else:
                    color = 'b'
                print(node.data, color, end=' ', sep='')

                if node.right:
                    inorderUtil(node.right)

        inorderUtil(node)
        print()

    def preorder(self):
        node = self.root

        def preorderUtil(node):
            if node != self.NIL:
                if node.color:
                    color = 'r'
                else:
                    color = 'b'
                print(node.data, color, end=' ', sep='')
                if node.left:
                    preorderUtil(node.left)
                if node.right:
                    preorderUtil(node.right)

        preorderUtil(node)
        print()

    def postorder(self):
        node = self.root

        def postorderUtil(node):
            if node != self.NIL:
                if node.left:
                    postorderUtil(node.left)
                if node.right:
                    postorderUtil(node.right)
                if node.color:
                    color = 'r'
                else:
                    color = 'b'
                print(node.data, color, end=' ', sep='')

        postorderUtil(node)
        print()

    def search(self, item):
        def searchUtil(root, item):
            if root is self.NIL:
                return self.NIL
            if root.data == item:
                return root
            if item < root.data:
                return searchUtil(root.left, item)
            # if item > root.data:
            else:
                return searchUtil(root.right, item)

        return searchUtil(self.root, item)

    def subtree_minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def subtree_maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node

    def successor(self, node):
        if node is self.NIL:
            return self.NIL
        if node.right != self.NIL:
            return self.subtree_minimum(node.right)
        else:
            current_node = node
            while current_node.parent != self.NIL and current_node.parent.left != current_node:
                current_node = current_node.parent
            if current_node.parent != self.NIL:
                return current_node.parent

    def predecessor(self, node):
        if node is self.NIL:
            return self.NIL
        if node.left is not self.NIL:
            return self.subtree_maximum(node.left)
        else:
            current_node = node
            while current_node.parent != self.NIL and current_node.parent.right != current_node:
                current_node = current_node.parent
            if current_node.parent != self.NIL:
                return current_node.parent

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, item):
        z = self.search(item)
        if z is self.NIL:
            return
        y = z
        y_original_color = y.color
        if z.left is self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.subtree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.deleteFixup(x)

    def deleteFixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root

            elif x == x.parent.right:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def max(self):
        node = self.root
        while node != self.NIL and node.right != self.NIL:
            node = node.right
        if node != self.NIL:
            return node.data
        raise ValueError('cannot find max in empty tree')

    def min(self):
        node = self.root
        while node != self.NIL and node.left != self.NIL:
            node = node.left
        if node != self.NIL:
            return node.data
        raise ValueError('cannot find min in empty tree')

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


t = RedBlackTree()

for x in range(21):
    t.insert(x)

t.inorder()
s = [x for x in range(21)]
shuffle(s)

for x in s:
    print(x)
    t.delete(x)
    t.inorder()
