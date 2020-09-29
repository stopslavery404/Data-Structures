# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:06:35 2020

@author: rahul
"""
'''point update and range minimum query'''
from math import ceil, log2
class SegmentTree:
    def __init__(self,arr):
        h=ceil(log2(len(arr)))
        self.max_size=2*(2**h)-1
        self.arr=[0]*self.max_size
        self.n=len(arr)
        self.construct(arr,0,self.n-1,0)
    
    def getMid(self,start,end):
        return (start+end)//2
    def construct(self,arr,start,end,index):
        if start==end:
            self.arr[index]=arr[start]
            return arr[start]
        mid=self.getMid(start,end)
        self.arr[index]=min(self.construct(arr,start,mid,2*index+1),self.construct(arr,mid+1,end,2*index+2))
        return self.arr[index]
    def getMin(self,l,r):
        if l<0 or r>self.n-1 or l>r:
            print('invalid Input')
            return float('None')
        def util(self,seg_start,seg_end,query_start,query_end,index):
            if query_start<=seg_start and query_end>=seg_end:
                return self.arr[index]
            if seg_end<query_start or seg_start>query_end:
                return float('inf')
            mid=self.getMid(seg_start,seg_end)
            return min(util(self,seg_start,mid,query_start,query_end,2*index+1),util(self,mid+1,seg_end,query_start,query_end,2*index+2))
        return util(self,0,self.n-1,l,r,0)
    def update(self,index,new_val):
        def util(self,seg_start,seg_end,index,new_val,seg_index):
            if index<seg_start or index>seg_end:
                return
            self.arr[seg_index]=new_val
            if seg_end!=seg_start:
                mid=self.getMid(seg_start,seg_end)
                util(self,seg_start,mid,index,new_val,2*seg_index+1)
                util(self,mid+1,seg_end,index,new_val,2*seg_index+2)
                self.arr[seg_index]=min(self.arr[2*seg_index+1],self.arr[2*seg_index+2])
        if index<0 or index>self.n-1:
            print('invalid input')
            return 
        util(self,0,self.n-1,index,new_val,0)
            
t=SegmentTree([1,2,3,4,5])
    