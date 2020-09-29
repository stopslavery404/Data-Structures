# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 03:31:30 2020

@author: rahul
"""

'''Sparse table for range Sum query 
    time complexity 
    O(n log(n)) preprocessing
    O(n log(n)) query
    
    segment tree is better for this
    '''
import math
st=[]
k=0

def build(arr):
    global st,k
    n=len(arr)
    k=math.floor(math.log2(n))+1
    st=[[0]*(k) for i in range(n)]
    for i in range(n):
        st[i][0]=arr[i]
    
    for j in range(1,k):
        i=0
        while i+(1<<j)<=n:
            st[i][j]=st[i][j-1]+st[i+(1<<j-1)][j-1]
            i+=1
    
def query(l,r):
    global k
    res=0
    for j in range(k,-1,-1):
        if (1<<j)<=r-l+1:
            res+=st[l][j]
            l+=(1<<j)
    return res

build([1,-3,4,6,2,0,3,5,7])
print(st)
print(query(0,5))