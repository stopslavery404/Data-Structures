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
    def __init__(self, arr=None):
        self.root = None
        if arr:
            if self.isSorted(arr):
                self.root=self.buildFromSorted(arr,0,len(arr)-1)
            else:
                from random import shuffle
                temp = [x for x in arr]
                shuffle(temp)
                for x in temp:
                    self.insert(x)
    def isSorted(self,arr):
        n=len(arr)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return False
        else:
            return True
    def buildFromSorted(self,arr,i,j):
        if i>j:
            return None
        mid=(i+j)//2
        root=Node(arr[mid])
        root.left=self.buildFromSorted(arr,i,mid-1)
        if root.left:
            root.left.parent=root
        root.right=self.buildFromSorted(arr,mid+1,j)
        if root.right:
            root.right.parent=root
        return root
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
        target = self.search(item)
        if target is None:
            return
        while target.right:
            successor = self.subtree_maximum(target)
            target.data, successor.data = successor.data, target.data
            target = successor

        if target.parent:
            if target.parent.left == target:
                target.parent.left = target.left
            else:
                target.parent.right = target.left
            target.left = None
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
'''
import time
s = time.time()
for x in range(2 ** 20):
    t.insert(x)
print('height of tree after 1Million insertions', t.height())

e = time.time()
print('time taken for 1Million insertions', e - s)

s = time.time()
for x in range(2 ** 20):
    t.delete(x)
e = time.time()
print('time taken for 1Million deletions', e - s)
'''
for x in [7, 4, 6, 8, 2, 1, 3, 5]:
    t.insert(x)
t.inorder()
t.delete(4)
t.inorder()
