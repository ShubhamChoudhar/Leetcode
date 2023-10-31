# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 
strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    def groupAnagrams(self, strs) -> str:
        anagram_groups = {}

        for word in strs:
            sorted_word = ''.join(sorted(word)) 

            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
                  
            else:
                anagram_groups[sorted_word] = [word] 

        return list(anagram_groups.values())  