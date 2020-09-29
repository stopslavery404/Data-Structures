# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:24:37 2020

@author: rahul
"""
class DisjointSet1:
    '''This one can take O(n) in worst case'''
    def __init__(self):
        self.parent=dict()

    def make_set(self,v):
        self.parent[v]=v
    def union_sets(self,a,b):
        a=self.find_set(a)
        b=self.find_set(b)
        if a!=b:
            self.parent[b]=a
    def find_set(self,v):
        if v==self.parent[v]:
            return v
        return self.find_set(self.parent[v])

class DisjointSet2:
    '''Using Path compression
    This one can take O(log n) in average case'''
    def __init__(self):
        self.parent=dict()

    def make_set(self,v):
        self.parent[v]=v
    def union_sets(self,a,b):
        a=self.find_set(a)
        b=self.find_set(b)
        if a!=b:
            self.parent[b]=a
    def find_set(self,v):
        if v==self.parent[v]:
            return v
        self.parent[v]=self.find_set(self.parent[v])
        return self.parent[v]

class DisjointSet3:
    '''Using path compression and union by size/rank
    This one can take O(log n) in worst case'''
    def __init__(self):
        '''based on union by size'''
        self.parent=dict()
        self.size=dict()

    def make_set(self,v):
        self.parent[v]=v
        self.size[v]=1
    def union_sets(self,a,b):
        a=self.find_set(a)
        b=self.find_set(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.parent[b]=a
            self.size[a]+=self.size[b]
    def find_set(self,v):
        if v==self.parent[v]:
            return v
        return self.find_set(self.parent[v])
class DisjointSet4:
    '''Using path compression and union by size/rank
    This one can take O(log n) in worst case'''
    def __init__(self):
        '''based on union by rank (depth of tree)'''
        self.parent=dict()
        self.rank=dict()

    def make_set(self,v):
        self.parent[v]=v
        self.rank[v]=0
    def union_sets(self,a,b):
        a=self.find_set(a)
        b=self.find_set(b)
        if a!=b:
            if self.rank[a]<self.rank[b]:
                a,b=b,a
            self.parent[b]=a
            if self.rank[a]==self.rank[b]:
                self.rank[a]+=1
    def find_set(self,v):
        if v==self.parent[v]:
            return v
        return self.find_set(self.parent[v])

class DisjointSet5:    
    '''Union by linking to random index
    Slightly slower than Union by rank/size'''
    def __init__(self):
        self.parent=dict()
        self.index=dict()

    def make_set(self,v):
        from random import random
        self.parent[v]=v
        self.index[v]=random()
    def union_sets(self,a,b):
        a=self.find_set(a)
        b=self.find_set(b)
        if a!=b:
            if self.index[a]<self.index[b]:
                a,b=b,a
            self.parent[b]=a
    def find_set(self,v):
        if v==self.parent[v]:
            return v
        return self.find_set(self.parent[v])

class DisjointSet6:    
    '''Union by flipping a coin
    much slower than union by rank/size/indexing
    lower bound (n*log(n)/(log log n) amortized
    '''
    def __init__(self):
        '''based on union by size'''
        self.parent=dict()

    def make_set(self,v):
        self.parent[v]=v
    def union_sets(self,a,b):
        from random import randint
        a=self.find_set(a)
        b=self.find_set(b)
        if a!=b:
            if randint(0,1):
                a,b=b,a
            self.parent[b]=a
    def find_set(self,v):
        if v==self.parent[v]:
            return v
        return self.find_set(self.parent[v])
