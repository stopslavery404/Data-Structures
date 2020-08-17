# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 00:03:39 2020

@author: rahul
"""



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:    
    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None
        
    def __repr__(self):
        arr=[]
        node=self.head
        while node:
            arr.append(node.data)
            node=node.next
        return str(arr)
    
    def __len__(self):
        return self.size
    
    def enqueue(self,data):
        if self.size==0:
            self.head=Node(data)
            self.tail=self.head
            self.size+=1
            return
        node=Node(data)
        self.tail.next=node
        self.tail=node
        self.size+=1
        return
    def front(self):
        if self.head:
            return self.head.data
    def dequeue(self):
        if self.size==0:
            raise Error('dequeue from empty queue')
        if self.size==1:
            result=self.head.data
            self.head=self.tail=None
            self.size-=1
            return result
        node=self.head
        result=node.data
        self.head=node.next
        self.size-=1
        if self.size==1:
            self.tail=self.head
        
        del(node)
        return result


class Error(Exception):
    pass
            

    