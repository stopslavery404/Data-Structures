# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:59:19 2020

@author: rahul
"""

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
        target_node = Node(item)
        prev_node = self.NIL
        current_node = self.root

        while current_node != self.NIL:
            prev_node = current_node
            if target_node.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        target_node.parent = prev_node
        if prev_node == self.NIL:
            self.root = target_node
        elif target_node.data < prev_node.data:
            prev_node.left = target_node
        else:
            prev_node.right = target_node
        target_node.left = self.NIL
        target_node.right = self.NIL
        target_node.color = RED
        self.insertFixup(target_node)

    def insertFixup(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
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

    def inorderSuccessor(self, node):
        if node == self.NIL:
            return self.NIL
        if node.right != self.NIL:
            return self.subtree_minimum(node.right)
        else:
            current_node = node
            while current_node.parent != self.NIL and current_node.parent.left != current_node:
                current_node = current_node.parent
            if current_node.parent != self.NIL:
                return current_node.parent

    def inorderPredecessor(self, node):
        if node == self.NIL:
            return self.NIL
        if node.left != self.NIL:
            return self.subtree_maximum(node.left)
        else:
            current_node = node
            while current_node.parent != self.NIL and current_node.parent.right != current_node:
                current_node = current_node.parent
            if current_node.parent != self.NIL:
                return current_node.parent

    def predecessor(self, key):
        if key < self.min():
            return None
        prev = None
        curr = self.root
        while curr != self.NIL and curr.data != key:
            prev = curr
            if key < curr.data:
                curr = curr.left
            elif key > curr.data:
                curr = curr.right
            else:
                break
        if curr != self.NIL:
            if curr.left != self.NIL:
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
        while curr != self.NIL and curr.data != key:
            prev = curr
            if key < curr.data:
                curr = curr.left
            elif key > curr.data:
                curr = curr.right
            else:
                break
        if curr != self.NIL:
            if curr.right != self.NIL:
                return self.subtree_minimum(curr.right)
            else:
                return self.inorderSuccessor(curr)
        elif prev.data > key:
            return prev
        return self.inorderSuccessor(prev)

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, item):
        target = self.search(item)
        if target is self.NIL:
            return
        prev_node = target
        original_color = prev_node.color
        if target.left is self.NIL:
            current_node = target.right
            self.transplant(target, target.right)
        elif target.right is self.NIL:
            current_node = target.left
            self.transplant(target, target.left)
        else:
            prev_node = self.subtree_minimum(target.right)
            original_color = prev_node.color
            current_node = prev_node.right
            if prev_node.parent == target:
                current_node.parent = prev_node
            else:
                self.transplant(prev_node, prev_node.right)
                prev_node.right = target.right
                prev_node.right.parent = prev_node
            self.transplant(target, prev_node)
            prev_node.left = target.left
            prev_node.left.parent = prev_node
            prev_node.color = target.color
        if original_color == BLACK:
            self.deleteFixup(current_node)

    def deleteFixup(self, current_node):
        while current_node != self.root and current_node.color == BLACK:
            if current_node == current_node.parent.left:
                sibling = current_node.parent.right
                if sibling.color == RED:
                    sibling.color = BLACK
                    current_node.parent.color = RED
                    self.left_rotate(current_node.parent)
                    sibling = current_node.parent.right
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    current_node = current_node.parent
                else:
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self.right_rotate(sibling)
                        sibling = current_node.parent.right
                    sibling.color = current_node.parent.color
                    current_node.parent.color = BLACK
                    sibling.right.color = BLACK
                    self.left_rotate(current_node.parent)
                    current_node = self.root
            elif current_node == current_node.parent.right:
                sibling = current_node.parent.left
                if sibling.color == RED:
                    sibling.color = BLACK
                    current_node.parent.color = RED
                    self.right_rotate(current_node.parent)
                    sibling = current_node.parent.left
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    current_node = current_node.parent
                else:
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self.left_rotate(sibling)
                        sibling = current_node.parent.left
                    sibling.color = current_node.parent.color
                    current_node.parent.color = BLACK
                    sibling.left.color = BLACK
                    self.right_rotate(current_node.parent)
                    current_node = self.root
        current_node.color = BLACK

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

    def height(self):
        def maxDepth(node):
            if node is None:
                return 0
            ldepth = maxDepth(node.left)
            rdepth = maxDepth(node.right)
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1

        return maxDepth(self.root)

    class Iterator:
        def __init__(self, root, NIL):
            self.node = root
            self.stack = []
            self.NIL = NIL

        def __next__(self):
            if self.node is self.NIL and not self.stack:
                raise StopIteration
            while self.node != self.NIL:
                self.stack.append(self.node)
                self.node = self.node.left
            self.node = self.stack.pop()
            item = self.node.data
            self.node = self.node.right
            return item

    def __iter__(self):
        return self.Iterator(self.root, self.NIL)


'''
t = RedBlackTree()
import time


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
print('time taken for 1Million searches', e-s)



s = time.time()
for x in range(2 ** 20):
    t.delete(x)
e = time.time()
print('time taken for 1Million deletions', e - s)
print(t.height())
'''
t = RedBlackTree([1, 2, 3, 4, 6, 7, 8])
t.inorder()
