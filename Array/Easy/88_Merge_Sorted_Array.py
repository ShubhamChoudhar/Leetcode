# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return(nums1.sort())
        if len(nums1) == 0:
            return(nums2.sort())
            
        for i in range(len(nums1)-1, m-1, -1):
            if nums1[i] == 0:
                nums1.pop(i)
        
        for i in range(0, n):
            nums1.append(nums2[i])
                
        nums1.sort()
        return(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

print(Solution().merge(nums1, nums2))

# Jab pop karte hai toh array length chota hote jata hai. Isliye loop piche se chalane ka taaki Index out of 
# range error nhi aaye.

# Intuition:
# We have to remove all the 0 elements from the nums1 array and append nums2 to nums1. Sort the nums1 array
# and return nums1

# Approach:
# First we will check if nums1 is empty or not. If it is empty then return nums2.sort and check if nums2 is empty.
# If it is empty then return nums1.sort. Otherwise, will iterate through nums1 in reverse order and check for 0
# element or number if it there then will be pop the element. After removing all the 0 elements from the nums1 
# array will iterate theough nums2 and append to nums1 array. return the nums1.sort.
# Time Complexity  - O(n)

# Video Link - https://www.youtube.com/watch?v=P1Ic85RarKY