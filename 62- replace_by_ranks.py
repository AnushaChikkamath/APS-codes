# -*- coding: utf-8 -*-
"""replace_by_ranks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfwrahhEYGANgbDN7DO3D3a-alw6Bler
"""

def changeArr(input1):

	newArray = input1.copy()
	
	newArray.sort()
	
	ranks = {}
	
	rank = 1
	
	for index in range(len(newArray)):
		element = newArray[index];
	
		if element not in ranks:
			ranks[element] = rank
			rank += 1
		
	# Assign ranks to elements
	for index in range(len(input1)):
		element = input1[index]
		input1[index] = ranks[input1[index]]


if __name__ == "__main__":
	
	arr = list(map(int, input().split()))
	changeArr(arr)
	
	print(arr)

