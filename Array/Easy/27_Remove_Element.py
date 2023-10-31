# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                                It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        
        return(len(nums))

nums = [3,2,2,3]
val = 3

# nums = [0,1,2,2,3,0,4,2]
# val = 2

print(Solution().removeElement(nums, val))

# Ismai bhi pop tha isliye peeche start kiya loop aur jitne bhi elements array mai value se milte the unko 
# remove kiya

# Intuition:
# The intuition will be more or less same as 26 problem. The only difference is to compare from target value.

# Approach:
# The approach is to iterate the loop in reverse order and compare the elements of the array with the target.
# If it is same then pop the element from the array. As in this we don't have to check for previous element
# of the array so if we pop and we are checking the last elemet of the array we don't have to increment or
# decrement the loop.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=Pcd1ii9P9ZI