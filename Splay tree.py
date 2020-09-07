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


class SplayTree:
    def __init__(self, arr=None):
        self.root = None
        self.size = 0
        if arr:
            from random import shuffle
            temp = [x for x in arr]
            shuffle(temp)
            for x in temp:
                self.insert(x)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:  # x is root
            self.root = y

        elif x == x.parent.left:  # x is left child
            x.parent.left = y

        else:  # x is right child
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:  # x is root
            self.root = y

        elif x == x.parent.right:  # x is right child
            x.parent.right = y

        else:  # x is left child
            x.parent.left = y

        y.right = x
        x.parent = y

    def insert(self, item):

        current = self.root
        previous = None
        while current:
            previous = current
            if item < current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(item)
        new_node.parent = previous
        if previous is None:
            self.root = new_node
        elif item < previous.data:
            previous.left = new_node
        else:
            previous.right = new_node
        self.size += 1
        self.splay(new_node)

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
        current = self.root
        while current and current.data != item:
            if item < current.data:
                current = current.left
            elif item > current.data:
                current = current.right
        if current:
            self.splay(current)
        return current

    def delete(self, key):
        target = self.search(key)
        if target is None:
            return
        left, right = target.left, target.right
        self.root = None
        sMax = None
        if left:
            left.parent = None
            sMax = self.subtree_maximum(left)
            self.splay(sMax)
            self.root = sMax
        if right:
            if left:
                sMax.right = right
            else:
                self.root = right
            right.parent = sMax
        self.size -= 1

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

    def splay(self, x):
        while x.parent != None:
            if x.parent == self.root:
                '''Zig'''
                if x.parent.left == x:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)

            elif x.parent.left == x and x.parent.parent.left == x.parent:
                '''zig-zig'''
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x.parent.right == x and x.parent.parent.right == x.parent:
                '''zig-zig'''
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x.parent.left == x and x.parent.parent.right == x.parent:
                '''zig-zag'''
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)
            elif x.parent.right == x and x.parent.parent.left == x.parent:
                'zig-zag'
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)

    def split(self, key):
        '''returns two trees with left tree having keys 
        less than or equal to key and right tree 
        having keys larger than key'''
        node = self.search(key)
        left = SplayTree()
        right = SplayTree()
        if not node:
            node = self.predecessor(key)
        if not node:
            right.root = self.root
            return left, right
        right_node = node.right
        right_node.parent = None
        node.right = None
        left.root = node
        right.root = right_node
        return (left, right)

    def merge(self, other):
        if self.root is None and other.root is None:
            return
        if self.root is None:
            self.root = other.root
            other.root = None
            return
        if other.root is None:
            return
        self.splay(self.subtree_maximum(self.root))
        other.splay(other.subtree_minimum(other.root))
        if other.root.data <= self.root.data:
            raise ValueError('incompaitable trees\nYou can try Union')
        self.root.right = other.root
        other.root.parent = self.root
        other.root = None

    def union(self, other):
        '''takes union of elements of two trees'''
        if other.root is None:
            return
        if self.root is None:
            self.root = other.root
            other.root = None
            return
        self.splay(self.subtree_maximum(self.root))
        other.splay(other.subtree_minimum(other.root))
        temp = None
        if other.root.data <= self.root.data:
            other.splay(other.successor(self.root.data))
            temp = SplayTree()
            temp.root = other.root.left
            other.root.left = None
            temp.root.parent = None
        self.root.right = other.root
        other.root.parent = self.root
        other.root = None
        if temp:
            for x in temp:
                self.insert(x)

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

    def __iter__(self):
        return self.Iterator(self.root)


t = SplayTree()

'''
s = time.time()
a = [x for x in range(2 ** 20)]
shuffle(a)
t = SplayTree(a)

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
'''
