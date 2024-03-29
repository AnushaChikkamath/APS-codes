# -*- coding: utf-8 -*-
"""longest_repeating_subsequence.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
import sys

#Longest repeating subsequence:
#Finding the length of the longest repeating subsequence such that the two 
#subsequences don't have the same string character at the same position

def longest_repeating_subsequence(strs,n):
  lrs=([[0 for i in range(n+1)] for j in range(n+1)])

  for i in range(0,n):
    lrs[0][i]=0

  for i in range(0,n):
    lrs[i][0]=0

  for i in range(1,n+1):
    for j in range(1,n+1):
      if(strs[i-1]==strs[j-1] and i!=j):
        lrs[i][j]=1+lrs[i-1][j-1]

      else:
        lrs[i][j]=max(lrs[i-1][j],lrs[i][j-1])

  return lrs[n][n]

def main():
  string1=input('Enter the string')
  n=len(string1)
  x=longest_repeating_subsequence(string1,n)
  print(f'The length of the longest repeating subsequence is {x}.')

if __name__=="__main__":
  main()

