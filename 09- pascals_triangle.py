# -*- coding: utf-8 -*-
"""pascals_triangle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
def pascals_triangle(n):
  final=[]
  for i in range(n):
    x=[]
    for j in range(0,i+1):
      m=(factorial(i)//(factorial(j)*factorial(i-j)))
      x.append(m)
    final.append(x)
  return final

def main():
  n=int(input("Enter n"))
  final=pascals_triangle(n)

  print(*final, sep = "\n")

if __name__=="__main__":
  main()

