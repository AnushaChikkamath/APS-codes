# -*- coding: utf-8 -*-
"""bit_difference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xX9h5ywVbAQHVxHbK_9lqAtnvWYpNhSK
"""

"""
  Bit Difference:

  You are given two numbers A and B. The task is to count the
  number of bits needed to be flipped to convert A to B.

  Input: A = 10, B = 20
  Output: 4

 A  = 01010
 B  = 10100  therefore, number of flipped bits= 4

"""

from typing import List

def bit_difference(num1,num2):
  xor= num1^num2
  count=0
  while xor>0:
    a=xor%2
    if(a==1):
      count=count+1
    xor=xor//2

  return count



def main():
  num1=int(input('Enter the first number'))
  num2=int(input('Enter the second number'))
  x=bit_difference(num1,num2)
  print(f'The number of bits that need to be flipped are {x}.')

if __name__=="__main__":
  main()
