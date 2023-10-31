class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            # Get the digits from the strings if available
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            # Calculate the sum of digits and carry
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            # Prepend the digit to the result
            result.insert(0, str(digit))

            i -= 1
            j -= 1

        return ''.join(result)

num1 = "11"
num2 = "123"

# num1 = "456"
# num2 = "77"

# num1 = "0"
# num2 = "0"

print(Solution().addStrings(num1, num2))