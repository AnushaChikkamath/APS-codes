# -*- coding: utf-8 -*-
"""longest_increasing_subsequence.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
import sys

#Finding the longest incraesing subsequence length in an array of elements
# for example - input : 5 11 3 15 30 25
#output- The longest increasing subsequence length - 4
def longest_increasing_subsequence(arr,n):
  lis=[1] * n

  for i in range(1,n):
    for j in range(0,i):
      if(arr[i]>arr[j] and lis[j]+1>lis[i]):
        lis[i]=lis[j]+1

  return max(lis)


def main():
  print('Enter the array of elements')
  arr = list(map(int, input().split()))
  n=len(arr)
  sequence=longest_increasing_subsequence(arr,n)
  print(f'The length of the longest increasing subsequence is {sequence}.')

if __name__=="__main__":
  main()
