# -*- coding: utf-8 -*-
"""stolen_value.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *

def stolen_value(arr):

  values=([0 for i in range(len(arr)+1)])
  values[0]=0
  values[1]=arr[0]

  for i in range(2,len(arr)+1):
    values[i]=max(values[i-1],values[i-2]+arr[i-1])

  return values[len(arr)]



def main():
  print('Enter the array of elements')
  arr = list(map(int, input().split()))
  sum=stolen_value(arr)
  print(f'The maximum value that can be obtained from stealing the houses is {sum}.')

if __name__=="__main__":
  main()

