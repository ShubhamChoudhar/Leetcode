class Solution:
    def rotate(self, nums, k) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())
            
        return(nums)

nums = [1,2,3,4,5,6,7]
k = 3

# nums = [-1,-100,3,99]
# k = 2

print(Solution().rot_arr(nums, k))

# In - place change karna hai isliye loop k tak chalao aur last element ko pop karke starting index pe insert kar do