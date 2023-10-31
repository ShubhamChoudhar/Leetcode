class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[::-1], s.split()))

s = "Let's take LeetCode contest"

print(Solution().reverseWords(s))