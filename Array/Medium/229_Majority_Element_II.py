class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        frequency = {}
        res = []
        for item in nums:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        
        for num in frequency:
            if frequency[num] > int(len(nums) / 3):
                res.append(num)
        
        return res

# nums = [3,2,3]
nums = [1]
# nums = [1,2]

print(Solution().majorityElement(nums))