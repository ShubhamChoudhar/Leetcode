class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        pairMap = {}
        count = 0
    
        for num in nums:
            if num in pairMap:
                pairMap[num] = pairMap[num] + 1
            else:
                pairMap[num] = 1

        if(k == 0):
            for num in pairMap:
                if pairMap[num] > 1:
                    count += 1
            
            return count
        
        for num in pairMap:
            if num - k in pairMap:
                count += 1

        return count
                
            

# nums = [3,1,4,1,5]
# k = 2

# nums = [1,2,3,4,5]
# k = 1

nums = [1,3,1,5,4]
k = 0

print(Solution().findPairs(nums, k))