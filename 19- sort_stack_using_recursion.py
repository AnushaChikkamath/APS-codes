# -*- coding: utf-8 -*-
"""sort_stack_using_recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
import sys

class Solution:
    def sortedInsert(self,stack, key):
        if not stack or key > stack[-1]:
            stack.append(key)
            return
        top = stack.pop()
        self.sortedInsert(stack, key)
        stack.append(top)
 
 
# Recursive method to sort a stack
    def sorted(self,stack):
        if not stack:
            return
        top = stack.pop()
        self.sorted(stack)
        self.sortedInsert(stack, top)

if __name__=="__main__":
  n=int(input('Enter n'))
  print('Enter the array elements')
  arr = list(map(int, input().split()))
  obj=Solution()
  obj.sorted(arr)
  print('The sorted stack is:')
  for e in range(len(arr)):
    print(arr.pop(),end=" ")

