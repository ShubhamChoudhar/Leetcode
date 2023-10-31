# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
# using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for l in s:
            if l not in sMap:
                sMap[l] = 1
            else:
                sMap[l] += 1
        
        for l in t:
            if l not in sMap:
                return False
            elif l not in tMap:
                tMap[l] = 1
            else:
                tMap[l] += 1
        
        if sMap == tMap:
            return True

s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s, t))

# Intuition:
# We have to find if s and t are anagrams of each other or not

# Approach:
# We will create hash map for s and t. If both the hash maps are same.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=9UtInBqnCgA