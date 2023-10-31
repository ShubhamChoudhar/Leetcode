# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        result = []

        for digit in reversed(digits):
            total = digit + carry
            print("Total:", total)
            carry = total // 10
            print("carry:", carry)
            result.append(total % 10)
            print("result:", result)

        if carry:
            result.append(carry)
            print("result:", result)

        return result[::-1]

# digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9]
digits = [9, 9]

print(Solution().plusOne(digits))

# Intuition:
# We have to add 1 to the number in the array or element. [1, 2, 3] will be considered as 123 and 123 + 1 = 124
# and 99 + 1 = 100.

# Approach:
# We will start with carry = 1 as we have to add 1 to the number. If we add 1 to the 1 to 8 number then there
# will be no carry but with 9 there will be carry. If carry is there we will save it in carry variable and append
# total % 10. 9 % 10 will be 9 but as we are adding 1 to the total before appending then 9 will be 10 and 
# 10 % 10 will be 0. Carry will be 1. We are appending carry also at last. Returning the reverse of the result
# array.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=jIaA8boiG1s