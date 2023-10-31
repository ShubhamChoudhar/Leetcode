# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums, target) -> int:
        prevMap = {}
        
        for i, n in enumerate(nums):
            if(target - n) in prevMap:
                return(prevMap[target - n], i)
        
            prevMap[n] = i

nums = [2]
target = 4

print(Solution().twoSum(nums, target))

# Intuition:
# The Two Sum problem asks us to find two numbers in an array that sum up to a given target value. We need to 
# return the indices of these two numbers.

# Approach:
# 1) Brute Force
# Using nested loops. The outer loop will iterate once for each element of the array whereas the inner loop will 
# iterate everytime over the array until we find the target or the outer loop increment by 1. 
# Time Complexity - O(n^2)
# 2) Hash Map
# We will append the array elements to the hash map as key and complement (target - element) of the element as 
# value. If complement is in hash map, we will return index of hash map and element (i).
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=KLlXCFG5TnA
