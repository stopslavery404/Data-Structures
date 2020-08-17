# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:34:47 2020

@author: rahul
"""

class TwoStacks:
    '''
    Stack is a linear data structure in which
    insert and delete operations are performed
    in constant time.

    It follows Last In First Out (LIFO)
    the element which is inserted last is the
    element which exits first.



    Time complexity
    push->      O(1)
    pop->       O(1)
    top->       O(1)
    isEmpty->   O(1)
    print->     O(maxsize)
    '''

    def __init__(self, maxsize):
        '''creates stack of max capacity maxsize'''
        self.__top1 = -1
        self.__top2=maxsize
        self.__arr = [0] * maxsize
        self.maxsize = maxsize
    def __repr__(self):
        return str(self.__arr)
    def isEmpty(self,stack_no):
        '''returns True if stack is empty'''
        if stack_no==1:
            return self.__top1 == -1
        elif stack_no == 2:
            return self.__top2==self.maxsize
    

    def push(self, item,stack_no):
        '''push an item into the stack
        example push(item)'''
        if stack_no == 1:
            if self.__top1 ==self.__top2-1 and self.__top1<self.maxsize:
                raise StackOverflow("Stack is full, can't push items.")
            self.__top1 += 1
            self.__arr[self.__top1] = item
        elif stack_no == 2:
            if self.__top2==self.__top1+1 and self.__top2>0:
                raise StackOverflow("stack is full, can't push items")
            self.__top2-=1
            self.__arr[self.__top2]=item

    def pop(self,stack_no):
        '''returns the top element and removes it from stack'''
        if stack_no == 1:            
            if self.isEmpty(1):
                raise StackUnderflow("Stack1 is empty, nothing to pop.")
            res=self.__arr[self.__top1] 
            self.__arr[self.__top1]=0    #not important but for security reasons
            self.__top1 -= 1
            return res
        elif stack_no == 2:
            if self.isEmpty(2):
                raise StackUnderflow('Stack2 is empty, nothing to pop.')
            res=self.__arr[self.__top2] 
            self.__arr[self.__top2]=0
            self.__top2+=1
            return res

    def top(self,stack_no):
        '''returns the top element without removing'''
        if stack_no == 1:
            if self.__top1 == -1:
                raise StackUnderflow('stack1 is empty')
            return self.__arr[self.__top1]
        if stack_no == 2:
            if self.__top2 == self.maxsize:
                raise StackUnderflow('stack2 is empty')
            return self.__arr[self.__top2]

    def __len__(self,stack_no):
        '''returns the length of stack with given stack number'''
        if stack_no == 1:
            return self.__top1 + 1
        elif stack_no==2:
            return self.maxsize-self.__top2
        


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass
