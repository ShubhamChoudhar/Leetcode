class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # duplicateMap = {}
        # duplicateArr = []

        # for num in nums:
        #     if num not in duplicateMap:
        #         duplicateMap[num] = len(duplicateMap)
        #     else:
        #         duplicateArr.append(num)
        
        # return duplicateArr
        res = []
        for i in range(len(nums)):
            
            indexToCheck = abs(nums[i]) - 1
            if nums[indexToCheck] < 0:
                res.append(abs(nums[i]))
            if nums[indexToCheck] > 0:
                nums[indexToCheck] = -1 * nums[indexToCheck]
                
        return res

nums = [4,3,2,7,8,2,3,1]
# nums = [1,1,2]
# nums = [1]

print(Solution().findDuplicates(nums))