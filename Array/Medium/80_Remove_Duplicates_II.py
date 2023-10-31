class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
                
        write_ptr = 2
        for read_ptr in range(2, len(nums)):
            if nums[read_ptr] != nums[write_ptr - 2]:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
                        
        return write_ptr

# Agar 2 ya do se kam hua array ka length toh utna hi return karna hai kyunki 2 baar koi bhi element repeat ho sakta hai. Hume changes
# 2 pointer ya index se karna hai isliye loop 2 index se start hua. Agar nums[write_ptr - 2] isliye likha hai kyunki 2 baar repeat ho
# sakta hai. Agar same nhi hua toh shift karna hai uska logic hai aur write_ptr ko increment karna hai. Agar same hua toh kuch nhi.


    # def rem_dup_2(nums):
    #     frequency = {}
    #     k = 0

    #     for num in nums:
    #         if num in frequency:
    #             if frequency[num] < 2:
    #                 frequency[num] += 1
            
    #         else:
    #             frequency[num] = 1
        
    #     for num in frequency:
    #         k = k + frequency[num]
        
    #     return (k)


nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))
# print(Solution().rem_dup_2(nums))