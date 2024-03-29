# -*- coding: utf-8 -*-
"""Fractional_Knapsack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQBoE_H6m4qF3Sjc3xblntUAR58GeS8N
"""

def fractional_knapsack(N,W,weight,value):

  index = list(range(N))
  ratio = [v/w for v, w in zip(value, weight)]

  index.sort(key=lambda i: ratio[i], reverse=True)
  remaining=W
  result=0
  for i in index:
    if(weight[i]<=remaining):
      result=result+value[i]
      remaining=remaining-weight[i]
    else:
      x=(remaining*value[i])/weight[i]
      result=result+x
      remaining=0
      break
  return result

def main():
  N=int(input("Enter the number of items"))
  print("Enter the weight of items")
  weight = list(map(int, input().split()))
  print("Enter the profit from items")
  value = list(map(int, input().split()))
  W=int(input('Enter the maximum weight of knapsack'))

  max_profit=fractional_knapsack(N,W,weight,value)
  print(f"The maximum profit to be obtained by adding items in the knapsack is {max_profit}")

if __name__=="__main__":
  main()

