class Solution:
    def canJump(self, nums) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
        return True


nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
# nums = [3,3,1,0,4]
# nums = [1,1,2,2,0,1,1]
# nums = [2,0,1,0,1]

print(Solution().canJump(nums))