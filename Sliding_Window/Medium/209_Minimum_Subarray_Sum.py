class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        min_length = len(nums)
        start = 0
        end = 0
        current_sum = 0

        if(sum(nums) < target):
            return 0

        while end < len(nums):
            current_sum = current_sum + nums[end]
            end += 1

            while start < end and current_sum >= target:
                current_sum = current_sum -  nums[start]
                start += 1

                min_length = min(min_length, end - start + 1)
        
        return min_length

# target = 7
# nums = [2,3,1,2,4,3]
target = 15
nums = [1,2,3,4,5]

print(Solution().minSubArrayLen(target, nums))