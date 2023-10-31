class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]

        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""
        for char, count in stack:
            res += (char * count)
        
        return res

s = "abcd"
k = 2
# s = "deeedbbcccbdaa"
# k = 3

print(Solution().removeDuplicates(s, k))

# Agar stack ka last element equal hai aane wale value se toh count 1 se increment karo. Initially hum
# character aur uska count 1 hi rakhenge. Agar count equal ho jata hai k se toh pop kardenge.
# Phir last mai joh characters hai stack uska uske count jitna res string mai add karenge aur return res.