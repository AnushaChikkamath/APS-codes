# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

def subsetSumToK(n,k,arr):
  #Forming the 2D dp table
  subset=([[False for i in range(k+1) ]for i in range(n+1) ])

  for i in range(1,k+1):
    subset[0][i]=False

  for i in range(0,n+1):
    subset[i][0]=True

  for i in range(1,n+1):
    for j in range(1,k+1):
      if(j<arr[i-1]):
        subset[i][j]=subset[i-1][j]
      else:
        subset[i][j]=(subset[i-1][j] or subset[i-1][j-arr[i-1]])

  return subset[n][k]


def main():
  n=int(input('Enter number of elements in array'))
  print('Enter the input array')
  arr = list(map(int, input().split()))
  k=int(input('Enter the value of subarray sum'))

  if(subsetSumToK(n,k,arr)):
    print('Yes, the subset sum can be formed')
  else:
    print('No, the subset sum cannot be formed')

if __name__== "__main__":
  main()

