# -*- coding: utf-8 -*-
"""buy_sell_stock_II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
import sys

#Best time to buy and sell stock- II
"""
  Can buy and sell stock any number of times
  Input- 7 1 5 3 6 4
  1. Buy at 1 and sell at 5 - profit: 4
  2. Buy at 3 and sell at 6 - profit: 3 
  Maximum Profit - 4+3 = 7

"""

def buy_sell_stock_II(arr,n):
  selling_date=0
  buy_date=0
  profit=0

  for i in range(1,n):
    if(arr[i]>=arr[i-1]):
      selling_date=selling_date+1
    
    else:
      profit=profit+arr[selling_date]-arr[buy_date]
      buy_date=selling_date=i
      

  profit=profit+arr[selling_date]-arr[buy_date]

  return profit


def main():
  print('Enter the stock prices')
  arr = list(map(int, input().split()))
  n=len(arr)
  x=buy_sell_stock_II(arr,n)
  print(f'The maximum profit that can be obtained by buying and selling stock any number of times from the given prices is {x}.')

if __name__=="__main__":
  main()

