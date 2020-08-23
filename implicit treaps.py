from random import random


def heapify(treap):
    if not treap:
        return
    max_ = treap
    if treap.left and treap.left.priority > max_.priority:
        max_ = treap.left
    if treap.right and treap.right.priority > max_.priority:
        max_ = treap.right
    if max_ != treap:
        treap.priority, max_.priority = max_.priority, t.priority
        heapify(max_)


class Treap:
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
        return self.Iterator(self)

    def __build(arr, i, j):
        if i == j:
            return None
        mid = (i + j) // 2
        treap = Treap(arr[mid])
        treap.left = Treap.__build(arr, i, mid)
        treap.right = Treap.__build(arr, mid + 1, j)
        heapify(treap)
        return treap

    def build(arr):
        '''generates treap using sorted array as input'''
        n = len(arr)
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                raise ValueError('input not sorted')
        return Treap.__build(arr, 0, n)

    def __init__(self, data):
        self.data = data
        self.size = 0
        self.priority = random()
        self.left = None
        self.right = None
        self.reversed = False

    def __repr__(self):
        s = ''
        if self.left:
            s += str(self.left)
        s += str(self.data) + ' '
        if self.right:
            s += str(self.right)
        return s

    def push(self):
        if self.reversed:
            self.reversed = False
            self.left, self.right = self.right, self.left
            if self.left:
                self.left.reversed ^= True
            if self.right:
                self.right.reversed ^= True

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

        return maxDepth(self)

    def update_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def inorder(self):
        def inorderUtil(node):
            if node:
                if node.left:
                    inorderUtil(node.left)
                print(node.data, end=' ')
                if node.right:
                    inorderUtil(node.right)

        inorderUtil(self)
        print()

    def preorder(self):
        def preorderUtil(node):
            if node:
                print(node.data, end=' ')
                if node.left:
                    preorderUtil(node.left)
                if node.right:
                    preorderUtil(node.right)

        preorderUtil(self)
        print()

    def postorder(self):
        def postorderUtil(node):
            if node:

                if node.left:
                    postorderUtil(node.left)
                if node.right:
                    postorderUtil(node.right)
                print(node.data, end=' ')

        postorderUtil(self)
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

        return searchUtil(self, item)

def size(root):
    if root:
        return root.size
    return 0
def merge(left, right):
    if left:
        left.push()
    if right:
        right.push()
    if not left or not right:
        treap = left or right
    elif left.priority > right.priority:
        left.right = merge(left.right, right)
        treap = left
    else:
        right.left = merge(left, right.left)
        treap = right
    treap.update_size()
    return treap


def split(treap, key, add=0):
    if not treap:
        return (None, None)
    treap.push()
    current_key = add + size(treap.left)
    if key <= current_key:
        left, treap.left = split(treap.left, key, add)
        right = treap
    else:
        treap.right, right = split(treap.right, key, add + 1 + size(treap.left))
        left = treap
    treap.update_size()
    return (left, right)


def reverse(treap, i, j):
    left, mid = split(treap, i)
    mid, right = split(mid, j + 1 - i)
    mid.reverse ^= True
    treap = merge(left, mid)
    treap = merge(treap, right)
    return treap


def extract(treap, start_index, end_index):
    mid, right = split(treap, end_index)
    left, mid = split(mid, start_index)
    treap = merge(left, right)
    return (treap, mid)


def insert(treap, pos, item):
    left, right = split(treap, pos)
    left = merge(left, Treap(item))
    treap = merge(left, right)
    return treap

def delete(treap, key):
    if not treap:
        return treap
    if treap.data == key:
        treap = merge(treap.left, treap.right)
        return treap
    else:
        if key < treap.data:
            treap.left = delete(treap.left, key)
        else:
            treap.right = delete(treap.right, key)
    return treap


def unite(x, y):
    if not x or not y:
        return x or y

    if x.priority < y.priority:
        x, y = y, x
    lt, rt = split(y, x.data)
    x.left = unite(x.left, lt)
    x.right = unite(x.right, rt)
    return x


