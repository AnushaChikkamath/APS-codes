# -*- coding: utf-8 -*-
"""non_decreasing_array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfwrahhEYGANgbDN7DO3D3a-alw6Bler
"""

# Time:  O(n)
# Space: O(1)

# Given an array with n integers, your task is to check if
# it could become non-decreasing by modifying at most 1 element.

#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first
# 4 to 1
# to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.

class Solution(object):
    def checkPossibility(self, nums):
       
        modified, prev = False, nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                if modified:
                    return False
                if i-2 < 0 or nums[i-2] <= nums[i]:
                    prev = nums[i]    # nums[i-1] = nums[i], prev = nums[i]
                else:
                    prev = nums[i-1]  # nums[i] = nums[i-1], prev = nums[i]
                modified = True
            else:
                prev = nums[i]
        return True
print(Solution().checkPossibility([4,2,3]))
print(Solution().checkPossibility([4,2,1]))

