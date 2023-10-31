class Solution:
    def canConstruct(self, ransomNote, magazine) -> bool:
        # frequency_map = {}
        # frequency = {}

        # for letter in ransomNote:
        #     if letter in frequency_map:
        #         frequency_map[letter] += 1
        #     else:
        #         frequency_map[letter] = 1
        
        # for letter in magazine:
        #     if letter in frequency:
        #         frequency[letter] += 1
        #     else:
        #         frequency[letter] = 1

        # for letter in frequency_map:
        #     if letter not in frequency or frequency_map[letter] > frequency[letter]:
        #         return False
        
        # return True

        frequency_map = {}
        for letter in magazine:
            if letter in frequency_map:
                frequency_map[letter] += 1
            else:
                frequency_map[letter] = 1

        for letter in ransomNote:
            if letter not in frequency_map or frequency_map[letter] <= 0:
                return False
            frequency_map[letter] -= 1
        
        return True


ransomNote = "a"
magazine = "b"
# ransomNote = "aa"
# magazine = "ab"
# ransomNote = "aa"
# magazine = "aab"

print(Solution().canConstruct(ransomNote, magazine))