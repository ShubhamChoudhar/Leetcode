# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to 
# the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            return 0

        leftSum = 0
        totalSum = sum(nums)  # Calculate the total sum of all elements
        
        for i in range(len(nums)):
            # Check if the left and right sums are equal
            if leftSum == (totalSum - leftSum - nums[i]):
                return i
            
            leftSum += nums[i]
        
        return -1

# nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
nums = [2, 1, -1]

print(Solution().pivotIndex(nums))

# Intuition:
# Find the index where the sum of left of that index is equal to the sum of right of that index.

# Approach:
# We will find the total sum of the array and Initialize left sum as 0. We will iterate through the loop and
# calculate the right sum of the array. We will compare right sum and left sum if it is equal then return i
# else we add the ith element or elemnent at that index to the left sum.
# Time Complexity  - O(n)

# Video Link - https://www.youtube.com/watch?v=u89i60lYx8U