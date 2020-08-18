# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:04:36 2020

@author: rahul
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    class Iterator:
        def __init__(self,head):
            self.current=head
        def __next__(self):
            if not self.current:
                raise StopIteration
            item=self.current.data
            self.current=self.current.next
            return item
    def __repr__(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next
        return str(arr)

    def __init__(self):
        self.size = 0
        self.head = None
        self.current=None

    def insert(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
            return
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return

    def insertAfter(self, prev_node, item):
        if not prev_node:
            raise Error('Previous node cannot be None')
        node = Node(item)
        node.prev = prev_node
        node.next = prev_node.next
        prev_node.next.prev = node
        prev_node.next = node

    def search(self, item):
        node = self.head
        while node and node.data != item:
            node = node.next
        return node

    def delete(self, item):
        node = self.search(item)

        if node:
            if node == self.head:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            del (node)
    def __iter__(self):
        return self.Iterator(self.head)



class Error(Exception):
    pass


l = SinglyLinkedList()
for x in [1, 2, 5, 4]:
    l.insert(x)
print(min(l))