# -*- coding: utf-8 -*-
"""Finding_duplicate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
import sys


#Slow and fast method to find duplicate in an array
#Time complexity- O(n)
def finding_only_duplicate(arr):
  fast=arr[0]
  slow=arr[0]
  while True:
    slow=arr[slow]
    fast=arr[arr[fast]]
    if(slow==fast):
      break
  
  fast=arr[0]
  while slow!=fast:
    fast=arr[fast]
    slow=arr[slow]
  return slow
  

def main():

  n=int(input('Enter the value of n'))
  print('Enter the array of elements')
  arr = list(map(int, input().split()))
  duplicate=finding_only_duplicate(arr)
  print(f'The only duplicate element present in the array is {duplicate}.')



if __name__=="__main__":
  main()

