# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:29:48 2020

@author: rahul
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.size = 0
        self.head = None

    def __repr__(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next
        return str(arr)

    def __len__(self):
        return self.size

    def push(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
            return
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
        return

    def top(self):
        if self.head:
            return self.head.data

    def pop(self):
        if self.size == 0:
            raise Error('Stack UnderFlow')
        if self.size == 1:
            self.head = None
            self.size -= 1
            return
        node = self.head
        self.head = node.next
        self.size -= 1
        del (node)


class Error(Exception):
    pass


s = Stack()
for x in [1, 2, 5, 4]:
    s.push(x)
