# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
# non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1

            i += 1
            j += 1
            if j == len(nums):
                break
        
        return nums

# nums = [0,1,0,3,12]
nums = [0]

print(Solution().moveZeroes(nums))

# Intuition:
# We have to move zeroes to the end of the array while keeping the other elements in the same order.

# Approach:
# We will initialize two variables i and j. The j variable is to keep count of the length of the array. We will
# iterate over the array and if we encounter 0 then append it to the nums array by popping the 0. Each time we
# will increment j. If we encounter 0 then decrement i and other if increment i to keep the i on the same index.
# If j == length of array then break the loop and return the array.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=aayNRwUN3Do