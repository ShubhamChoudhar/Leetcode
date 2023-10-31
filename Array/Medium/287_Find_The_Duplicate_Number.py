class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Approach 1
        # duplicateNumber = {}
        # for num in nums:
        #     if num in duplicateNumber:
        #         return num
        #     duplicateNumber[num] = len(duplicateNumber)

        # Approach 2
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        # Approach 3 Floyd's algorithm Totortise and Hare formula
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow

nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
print(Solution().findDuplicate(nums))