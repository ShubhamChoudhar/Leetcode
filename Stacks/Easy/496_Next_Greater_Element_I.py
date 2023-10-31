class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # next_greater_element_map = {}
        # next_greater_element_stack = []

        # for i in range(len(nums2)):
        #     if nums2[i] in nums1:
        #         j = i + 1
        #         if j == len(nums2):
        #             next_greater_element_map[nums2[i]] = -1
        #             break
        #         while j < len(nums2) and nums2[i] >= nums2[j]:
        #             j += 1
        #             if j == len(nums2):
        #                 next_greater_element_map[nums2[i]] = -1
        #                 break
                
        #         else:
        #             next_greater_element_map[nums2[i]] = nums2[j]
            
        # print("next_greater_element_map:", next_greater_element_map)
        
        # for i in range(len(nums1)):
        #     next_greater_element_stack.append(next_greater_element_map[nums1[i]])
        
        # return next_greater_element_stack

        next_greater_element_map = {}
        stack = []

        # Iterate through nums2 in reverse order.
        for num in reversed(nums2):
            print("Num2:", num)
            while stack and num >= stack[-1]:
                l = stack.pop()  # Pop elements from the stack until we find a greater element.
                print("Popped Element:", l)
            if stack:
                next_greater_element_map[num] = stack[-1]  # The next greater element.
                print("Stack[-1]:", stack[-1])
            else:
                next_greater_element_map[num] = -1
            stack.append(num)  # Add the current element to the stack.

        next_greater_element_stack = [next_greater_element_map[num] for num in nums1]

        return next_greater_element_stack
                        


nums1 = [4,1,2]
nums2 = [1,3,4,2]

# nums1 = [2,4]
# nums2 = [1,2,3,4]

print(Solution().nextGreaterElement(nums1, nums2))