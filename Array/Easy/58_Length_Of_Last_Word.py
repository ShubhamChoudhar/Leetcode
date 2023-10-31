# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution:
    def lenoflastword(self, s):
        words = s.split()
        print("words:", words)
        return len(words[len(words) - 1])

s = "   fly me   to   the moon  "
s1 = "luffy is still joyboy"
s3 = "Hello World"

print(Solution().lenoflastword(s3))

# Intuition:
# We have to find the length of the last word.

# Approach:
# Create a list of words in a string wirh space seperated. Then return the length of last word.

# Video Link - https://www.youtube.com/watch?v=KT9rltZTybQ