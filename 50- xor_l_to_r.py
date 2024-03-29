# -*- coding: utf-8 -*-
"""xor_L_to_R.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U_QyT8VlAu2EmXdD-cmrgPjjIkgLUgvU
"""

"""
  Find XOR of numbers from L to R:-

  You are given two integers L and R, your task is to find the XOR of 
  elements of the range [L, R].

  Input: L = 4, R = 8 
  Output: 8 

  Time Complexity- O(1)


"""

from operator import xor

def find(n):
    x=n%4
    
    if(x==0):
        return n
    elif(x==1):
        return 1
    elif(x==2):
        return n+1
    elif(x==3):
        return 0
        
class Solution:
    def findXOR(self, l, r):
        return (xor(find(l-1),find(r)))

a,b=(map(int,input().split()))
ob=Solution()
ans=ob.findXOR(a,b)
print(ans)

