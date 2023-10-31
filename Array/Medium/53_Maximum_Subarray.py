class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0

            currSum += nums[i]
            maxSum = max(maxSum, currSum)
        
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]