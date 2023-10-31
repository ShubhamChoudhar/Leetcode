# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number 
# sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sqrt_nums = []
        for num in nums:
            sqrt_nums.append(num * num)
        
        return sorted(sqrt_nums)

nums = [-4,-1,0,3,10]
# nums = [-7,-3,2,3,11]

print(Solution().sortedSquares(nums))

# Intuition:
# Find the squares of each number in an array and sort the array.

# Approach:
# 1) Approach 1
# Iterate through the array. Multiple each element by itself append it to new array. Sort the array and return the
# array
# Time Complexity: O(nlog(n))

# Video Link - https://www.youtube.com/watch?v=FPCZsG_AkUg