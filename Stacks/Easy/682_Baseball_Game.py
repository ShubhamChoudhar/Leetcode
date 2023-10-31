class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for op in operations:
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * int(stack[-1]))
            else:
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
    
        return sum(stack)

            

# ops = ["5", "+", "C", "D", "-2"]
# ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(ops))