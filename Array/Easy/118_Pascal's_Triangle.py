# Given an integer numRows, return the first numRows of Pascal's triangle.

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            
            res.append(row)
        
        return res

numRows = 5
# numRows = 1

print(Solution().generate(numRows))

# Intuiton:
# We have to create a pascal's triangle with given number of rows.

# Approach:
# The first row id [[1]]. So, we will initialize the res with [[1]]. We will iterate through number of rows.
# We will initilize another array with temp having [0] at starting and [0] at ending with res last subarray.
# And row ith empty array. We will iterate through len of res last subarray and kepp on appending the
# addition of temp j index and j + 1 index. After iterating through all the elements of temp we will
# append the row array to res array.
# Time Complexity - O(n^2).

# Video Link - https://www.youtube.com/watch?v=nPVEaB3AjUM