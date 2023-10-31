class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
    
        stack = []
        in_stack = set()

        for idx, char in enumerate(s):
            if char not in in_stack:
                # If the current character is smaller than the last character in the stack
                # and the last character in the stack has another occurrence later
                while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                    # Remove the last character from the stack
                    in_stack.remove(stack.pop())
                stack.append(char)
                in_stack.add(char)
        
        return ''.join(stack)

# s = "bcabc"
s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))