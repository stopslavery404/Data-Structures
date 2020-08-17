# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 00:16:21 2020

@author: rahul
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next
        return str(arr)

    def __len__(self):
        return self.size

    def appendleft(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return

    def append(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        node = Node(data)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1
        return

    def pop(self):
        if self.size == 0:
            raise Error('dequeue from empty queue')
        if self.size == 1:
            result = self.tail.data
            self.head = self.tail = None
            self.size -= 1
            return result
        result = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        if self.size == 1:
            self.tail = self.head

        del (node)
        return result

    def popleft(self):
        if self.size == 0:
            raise Error('dequeue from empty queue')
        if self.size == 1:
            result = self.head.data
            self.head = self.tail = None
            self.size -= 1
            return result
        result = self.head.data
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        if self.size == 1:
            self.tail = self.head

        del (node)
        return result


class Error(Exception):
    pass
