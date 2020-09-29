# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:34:01 2020

@author: rahul
"""

stack=[]
def add(item):
    if stack:
        stack.append((item,min(item,stack[-1][1])))
    else:
        stack.append((item,item))
def pop():
    return stack.pop()[0]
def minimum():
    return stack[-1][1]


    