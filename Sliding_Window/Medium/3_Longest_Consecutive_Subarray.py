class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_subarray = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(longest_subarray):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)

            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength

# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"

print(Solution().lengthOfLongestSubstring(s))