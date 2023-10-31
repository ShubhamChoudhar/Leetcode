import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv
            }
        
        result = []
        def isNum(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        for token in tokens:
            if isNum(token):
                result.append(int(token))
            else:
                num1 = result.pop()
                num2 = result.pop()
                result.append(int(ops[token](num2, num1)))
        
        return result[0]
            

# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))