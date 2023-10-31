# Given an integer array nums, return true if any value appears at least twice in the array, and return false 
# if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums) -> bool:
        num_count = {}
        for num in nums:
            if num in num_count:
                return True 
            else:
                num_count[num] = 1
        
        return False

nums = [1,1,1,3,3,4,3,2,4,2]

print(Solution().containsDuplicate(nums))

# Intuition:
# Find if any duplicate element is present in the array or not.

# Approach:
# We will start creating the hash map and if the element is not present in hash map append the element to the 
# hash map. If it is present in the hash map then return True. If we iterate over the whole array and could not
# find the duplicate element then return False.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=3OamzN90kPg