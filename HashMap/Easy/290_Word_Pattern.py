class Solution:
    def wordPattern(self, pattern, s) -> bool:
        map_string = {}
        x = ""
        t = [letter for letter in s.split()]

        if len(t) > len(pattern) or len(t) < len(pattern):
            return False

        for i in range(len(t)):
            if t[i] not in map_string and pattern[i] not in map_string.values():
                map_string[t[i]] = pattern[i]
        
        print(map_string)
        
        for i in range(len(t)):
            if t[i] in map_string:
                x = x + map_string[t[i]]

        print(x)
        print(s.replace(" ", ""))
        
        if x == pattern:
            return True
        
        return False

# pattern = "abba"
# s = "dog cat cat dog"
# pattern = "abba"
# s = "dog dog dog dog"
# pattern = "jquery"
# s = "jquery"
pattern = "abba"
s = "dog cat cat fish"
print(Solution().wordPattern(pattern, s))