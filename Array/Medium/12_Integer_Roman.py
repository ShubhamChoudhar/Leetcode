class Solution:
    def intToRoman(self, num) -> str:
        roman_int = {
        'M': 1000,
        'D': 500,
        'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1
        }
        val = ""

        for roman, int in roman_int.items():
            if (num // int) > 0:
                print("Roman:", roman)
                print("Int:", int)
                val += roman
                print("Val:", val)
                num = num % int
                print("Num after rem:", num)
                if num == 0:
                    break
        
        return val

num = 90
print(Solution().intToRoman(num))