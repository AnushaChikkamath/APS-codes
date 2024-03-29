# -*- coding: utf-8 -*-
"""minimum_jumps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xX9h5ywVbAQHVxHbK_9lqAtnvWYpNhSK
"""

"""
  Jump game-

  Given an array where each index marks the number of jumps that
  can be taken from that index, then find the number of minimum
  number of jumps required to reach the end of the array.

  Input- [2,3,1,1,4] 
  Output- 2

  Input- [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
  Output - 3

"""

from typing import List

def jump_game(arr,n):
  if(arr[0]==0):
    return -1

  if(n==1):
    return 0
  
  maximum_reach=arr[0]
  steps=arr[0]
  count=1
  i=1
  while(i<=n-2):
      maximum_reach=max(maximum_reach,i+arr[i])
      steps=steps-1
      if(steps==0):
          count=count+1
          if(i>=maximum_reach):
              return -1
          steps=maximum_reach-i
      i=i+1
  return count

  
def main():
  print('Enter the array elements')
  arr = list(map(int, input().split()))
  n=len(arr)
  x=jump_game(arr,n)
  if(x==-1):
    print(f'The end of the array cannot be reached.')
  else:
    print(f'The minimum number of jumps required to reach the end of the array is {x}.')
  

if __name__=="__main__":
  main()

