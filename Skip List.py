from random import randint


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.data = data


class Skiplist:
    def __init__(self):
        self.left_top = Node(float('-inf'))
        self.right_top = Node(float('inf'))
        self.left_top.right = self.right_top
        self.right_top.left = self.left_top

    def search(self, data):
        curr = self.left_top
        while True:
            while curr.right.data < data:
                curr = curr.right
            if curr.bottom is None:
                break
            curr = curr.bottom

        if curr.right.data == data:
            return curr.right
        return None

    def insert(self, data):
        stack = []
        curr = self.left_top
        while True:
            while curr.right.data < data:
                curr = curr.right
            if curr.bottom is None:
                break
            stack.append(curr)

            curr = curr.bottom
        if curr.right.data == data:
            return

        new_node = Node(data)
        new_node.right = curr.right
        new_node.right.left = new_node
        new_node.left = curr
        curr.right = new_node
        curr = new_node

        while randint(0, 1) == 1:

            if stack:
                prev = stack.pop()
                new_node = Node(data)
                curr.top = new_node
                new_node.bottom = curr
                curr = new_node
                curr.left = prev
                curr.right = prev.right
                prev.right = curr
                curr.right.left = curr
            else:
                new_node = Node(data)
                curr.top = new_node
                curr.top.bottom = curr
                curr = new_node
                curr.right = Node(float('inf'))
                curr.right.left = curr
                curr.left = Node(float('-inf'))
                curr.left.right = curr
                curr.left.bottom = self.left_top
                self.left_top.top = curr.left
                self.left_top = curr.left
                curr.right.bottom = self.right_top
                self.right_top.top = curr.right
                self.right_top = curr.right

    def delete(self, data):
        curr = self.search(data)
        if curr is None:
            return
        while curr:
            curr.left.right = curr.right
            curr.right.left = curr.left
            curr = curr.top
            if curr:
                del (curr.bottom)

    def __str__(self):
        s = ''
        lmost = self.left_top

        while lmost:
            curr = lmost
            while curr:
                s += str(curr.data) + '  '
                curr = curr.right
            s += '\n'
            lmost = lmost.bottom
        return s
    def height(self):
        h=0
        node=self.left_top
        while node.bottom:
            h+=1
            node=node.bottom
        return h



import time

t = Skiplist()
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

