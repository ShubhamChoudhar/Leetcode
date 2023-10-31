class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        validParanthesis = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        for paran in s:
            if paran == '(' or paran == '[' or paran == '{':
                result.append(paran)
            
            if paran == ')' or paran == ']' or paran == '}':
                if len(result) > 0:
                    if validParanthesis[paran] == result[-1]:
                        result.pop()
                
                    else:
                        return False
                
                else:
                    return False
        
        if len(result) == 0:
            return True


# s = "()"
s = "()[]{}"
# s = "(]"
print(Solution().isValid(s))

# Ek hashmap create kiya jaha par band paranthesis map kar kar raha khule huye paranthesis ko. Phir hum stack mai aapend karna chalu 
# karenge tab tak ki hume band paranthesis nhi mil jata aur agar last element in stack mapped hai aane wale paranthesis toh pop kar denge.
# End mai agar stack khali hai toh valid paranthesis hai nhi hai toh valid paranthesis nhi hai.