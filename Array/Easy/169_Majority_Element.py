# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority 
# element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        frequency = {}
        for item in nums:
            if item in frequency:
                frequency[item] += 1
                if frequency[item] > int(len(nums) / 2):
                    return item
            else:
                frequency[item] = 1

nums = [3,2,3]
# nums = [2,2,1,1,1,2,2]

print(Solution().majorityElement(nums))

# Intuition:
# We have to find the number of elements that are repeated or have duplicates in the array and number of duplicate
# elements is greater than n / 2 or len of array / 2.

# Approach:
# Find the frequency of each element in the array using hash map and iterate through the hash map. The value which
# satisfies the condition return the key.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=7pnhv842keE