class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        map_min_index = {}

        for index, num in enumerate(nums):
            if num not in map_min_index:
                map_min_index[num] = [1, index]
            else:
                map_min_index[num][0] += 1
                # print("Index", index)
                # print(map_min_index[num][1])
                # print(abs(index - map_min_index[num][1]))
                if abs(index - map_min_index[num][1]) <= k:
                    return True
                else:
                    map_min_index[num][1] = index
        
        print(map_min_index)
        
        for num in map_min_index:
            if map_min_index[num][0] > 1 and map_min_index[num][1] <= k:
                return True
        
        return False
            
      
        
        # print(map_min_index)
        
        # for num in map_min_index:
        #     if map_min_index[num] <= k:
        #         return True
        
        # return False

# def two_values(nums):

#     frequency_map = {}

#     for index, num in enumerate(nums):
#         if num not in frequency_map:
#             frequency_map[num] = [1, index]
#         else:
#             frequency_map[num][0] += 1  # Increment the frequency
#             frequency_map[num][1] = index  # Update the last occurrence index
    
#     print((frequency_map[1])[0])

#     return frequency_map


# Test with a sample list
# nums = [1, 2, 3, 2, 3, 3, 4]
# nums = [1,0,1,1]
# print(two_values(nums))

nums = [1,2,3,1]
k = 3
# nums = [1,0,1,1]
# k = 1
# nums = [1,2,3,1,2,3]
# k = 2
# nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
# k = 1

print(Solution().containsNearbyDuplicate(nums, k))