# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = []
        # rSum = 0
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            if i == 0:
                runningSum.append(nums[i])
            else:
                runningSum.append(runningSum[i - 1] + nums[i])

        # for num in nums:
        #     rSum += num
        #     runningSum.append(rSum)
        
        return runningSum


# nums = [1,2,3,4]
# nums = [1,1,1,1,1]
nums = [3,1,2,10,1]

print(Solution().runningSum(nums))

# Intuition:
# Find the running sum of each element in an array.

# Approach:
# 1) Approach 1
# Initialize an array and a variable as 0. Iterate through the array and add the element to the variable i.e. rSum
# Append the rSum to the array. Return the array.
# 2) Approach 2
# Iterate through the array using index or range. Append the sum directly to array without rSum. Adding the 
# previous and current index value.
# The approach 2 is faster and efficient in space also as we are not using rSum and not computing rSum each time.

# Video Link - https://www.youtube.com/watch?v=fFJaIDUKDoA&t=238s