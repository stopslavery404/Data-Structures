# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 01:39:03 2020

@author: rahul
"""
'''Sparse table for rmq 
    time complexity 
    O(n log(n)) preprocessing
    O(1) query
    '''
import math
st=[]

def build(arr):
    global st
    n=len(arr)
    k=math.floor(math.log2(n))+1
    st=[[0]*(k) for i in range(n)]
    for i in range(n):
        st[i][0]=arr[i]
    
    for j in range(1,k):
        i=0
        while i+(1<<j)<=n:
            st[i][j]=min(st[i][j-1],st[i+(1<<j-1)][j-1])
            i+=1
    
def query(l,r):
    j=int(math.log2(r-l+1))
    res=min(st[l][j],st[r-(1<<j)+1][j])
    return res

build([1,-3,4,6,2,0,3,5,7])
print(st)
print(query(3,3))