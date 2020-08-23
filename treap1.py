from random import random

def heapify(treap):
    if not treap:
        return
    max_=treap
    if treap.left and treap.left.priority>max_.priority:
        max_=treap.left
    if treap.right and treap.right.priority > max_.priority:
        max_=treap.right
    if max_!=treap:
        treap.priority,max_.priority = max_.priority,t.priority
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
    def __build(arr,i,j):
        if i==j:
            return None
        mid=(i+j)//2
        treap=Treap(arr[mid])
        treap.left=Treap.__build(arr,i,mid)
        treap.right=Treap.__build(arr,mid+1,j)
        heapify(treap)
        return treap
    def build(arr):
        '''generates treap using sorted array as input'''
        n=len(arr)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                raise ValueError('input not sorted')
        return Treap.__build(arr,0,n)
    def __init__(self, data):
        self.data = data
        self.priority = random()
        self.left = None
        self.right = None


    def __repr__(self):
        s = ''
        if self.left:
            s += str(self.left)
        s += str(self.data) + ' '
        if self.right:
            s += str(self.right)
        return s

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


def merge(left, right):
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        
        left.right = merge(left.right, right)
        return left
    else:
        
        right.left = merge(left, right.left)
    return right





def split(treap, key):
    
    if not treap:
        return (None, None)
    if not key:
        return (None,treap)
    elif key < treap.data:
        left, treap.left = split(treap.left, key)
        right = treap
    else:
        treap.right, right = split(treap.right, key)
        left = treap
    return (left, right)


def extract(treap, start_index, end_index):
    mid, right = split(treap, end_index)
    left, mid = split(mid, start_index)
    treap = merge(left, right)
    return (treap, mid)


def insert(treap,item):
    def util(t,it):
        if not t:
            t=it
            return t
        elif it.priority>t.priority:
            it.left,it.right=split(t,it.data)
            t=it
            return t
        else:
            if it.data<t.data:
                t.left=util(t.left,it)
            else:
                t.right=util(t.right,it)
            return t
    return util(treap,Treap(item))

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


t=Treap(0)
import time

s = time.time()
for x in range(2 ** 20):
    t=insert(t,x)
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
    t=delete(t,x)
e = time.time()
print('time taken for 1Million deletions', e - s)
