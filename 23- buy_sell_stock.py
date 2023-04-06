# -*- coding: utf-8 -*-
"""buy_sell_stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

from math import *
import sys

#Best time to buy and sell stock
"""
  Input- 1 2 3 4
  Best time to buy stock would be at time t=0
  Best time to sell stock would be at time t=3
  Maximum Profit - 4-1 = 3

"""

def buy_sell_stock(arr,n):
  buy=arr[0]
  max_profit=0

  for i in range(1,n):
    if(arr[i]<buy):
      buy=arr[i]

    elif(arr[i]-buy>max_profit):
      max_profit=arr[i]-buy

  return max_profit


def main():
  print('Enter the stock prices')
  arr = list(map(int, input().split()))
  n=len(arr)
  x=buy_sell_stock(arr,n)
  print(f'The maximum profit that can be obtained by buying and selling stock once from the given prices is {x}.')

if __name__=="__main__":
  main()
