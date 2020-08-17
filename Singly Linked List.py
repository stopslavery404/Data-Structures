# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:04:52 2020

@author: rahul
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __repr__(self):
        arr=[]
        node=self.head
        while node:
            arr.append(node.data)
            node=node.next
        return str(arr)
    def __init__(self):
        self.size=0
        self.head=None
    
    def insert(self,data):
        if self.size==0:
            self.head=Node(data)
            self.size+=1
            return
        node=Node(data)
        node.next = self.head
        self.head=node
        self.size+=1
        return
    def insertAfter(self,prev_node,item):
        if not prev_node:
            raise Error('Previous node cannot be None')
        node=Node(item)
        node.next=prev_node.next
        prev_node.next=node
    def search(self,item):
        node=self.head
        while node and node.data!=item:
            node=node.next
        return node
    def delete(self,item):
        prev_node=self.head
        next_node=prev_node.next
        if prev_node.data==item:
            self.head=next_node
            del(prev_node)
            return
        
        while next_node and next_node.data!=item:
            prev_node = next_node
            next_node = next_node.next
        if next_node:
            prev_node.next=next_node.next
            del (next_node)

class Error(Exception):
    pass
            
        
l=SinglyLinkedList()
for x in [1,2 ,5,4]:
    l.insert(x)
