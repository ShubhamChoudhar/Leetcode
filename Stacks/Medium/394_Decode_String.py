class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((num, current_str))
                num = 0
                current_str = ""
            elif char == "]":
                prev_num, prev_str = stack.pop()
                current_str = prev_str + prev_num * current_str
            else:
                current_str += char

        return current_str

s = "3[a]2[bc]"
# s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"

print(Solution().decodeString(s))
