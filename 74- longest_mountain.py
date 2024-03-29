# -*- coding: utf-8 -*-
"""longest_mountain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfwrahhEYGANgbDN7DO3D3a-alw6Bler
"""

# Let's call any (contiguous) subarray B (of A) a mountain
# if the following properties hold:
#
# B.length >= 3
# There exists some 0 < i < B.length - 1
# such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.

# Time:  O(n)
# Space: O(1)
# Example 1:

# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.





class Solution(object):
    def longestMountain(self, A):
        result, up_len, down_len = 0, 0, 0
        for i in range(1, len(A)):
            if (down_len and A[i-1] < A[i]) or A[i-1] == A[i]:
                up_len, down_len = 0, 0
            up_len += A[i-1] < A[i]
            down_len += A[i-1] > A[i]
            if up_len and down_len:
                result = max(result, up_len+down_len+1)
        return result

arr = list(map(int, input().split()))
print(Solution().longestMountain(arr))

