# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each 
# number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a
        
        if n == 1:
            return b
        
        # while n >= 2:
        #     c = a + b
        #     a = b
        #     b = c
        #     n -= 1
        
        # return c

        self.fib(n - 1) + self.fib(n - 2)

# n = 2
# n = 3
# n = 4
# n = 6
n = 7

print(Solution().fib(n))

# Intuition:
# We have to find the fibonnaci number of the given n

# Approach:
# 1) Without Recursion
# Initialize two variable a and b as 0 and 1 respectively. If n == 0 then return 0 and if n == 1 then return 1.
# If any other number then c = a + b. a = b and b = c. It will iterate through the from 2 to n.
# Time Complexity - O(n)

# 2) With Recursion
# If n == 0 then return 0 and if n == 1 then return 1. Create a recursive function self.fib(n - 1) + self.fib(n - 2)
# Time Complexity - O(2^n)
# Time Complexity wise the approach with without recursice is better

# Video Link - https://www.youtube.com/watch?v=dDokMfPpfu4