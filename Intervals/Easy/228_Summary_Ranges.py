class Solution:
    def summaryRanges(self, nums) -> list[str]:
        # start = 0
        # end = 1
        # temp = []

        # if len(nums) == 0:
        #     return temp

        # if len(nums) == 1:
        #    temp.append(str(nums[0]))
        #    return temp

        # while end < len(nums):
        #     if nums[end] - nums[end - 1] == 1:
        #         end += 1
            
        #     elif nums[end] - nums[end - 1] != 1 and (end - start) > 1:
        #         temp.append(str(nums[start]) + "->" + str(nums[end - 1]))
        #         start = end
        #         end += 1
        #         print(4567)
        #         print("Start in elif:", start)
        #         print("End in elif:", end)

        #     else:
        #         temp.append(str(nums[start]))
        #         start = end
        #         end += 1
        #         print("Start in else:", start)
        #         print("End in else:", end)
            
        # if start == end - 1:
        #     temp.append(str(nums[start]))
        # else:
        #     temp.append(str(nums[start]) + "->" + str(nums[end - 1]))
        
        # return temp

        if not nums:
            return []

        start = 0
        end = 1
        temp = []

        while end <= len(nums):
            if end < len(nums) and nums[end] - nums[end - 1] == 1:
                end += 1
            else:
                if start == end - 1:
                    temp.append(str(nums[start]))
                else:
                    temp.append(str(nums[start]) + "->" + str(nums[end - 1]))
                start = end
                end += 1

        return temp

# nums = [0,1,2,4,5,7]
# nums = [0,2,3,4,6,8,9]
nums = [-1]
print(Solution().summaryRanges(nums))