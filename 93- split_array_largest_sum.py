# -*- coding: utf-8 -*-
"""split_array_largest_sum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfwrahhEYGANgbDN7DO3D3a-alw6Bler
"""

# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.




class Solution(object):
    def splitArray(self, nums, m):
        
        def canSplit(nums, m, s):
            cnt, curr_sum = 1, 0
            for num in nums:
                curr_sum += num
                if curr_sum > s:
                    curr_sum = num
                    cnt += 1
            return cnt <= m

        left, right = 0, 0
        for num in nums:
            left = max(left, num)
            right += num

        while left <= right:
            mid = left + (right - left) // 2;
            if canSplit(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

print(Solution().splitArray([7,2,5,10,8],2))

# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

