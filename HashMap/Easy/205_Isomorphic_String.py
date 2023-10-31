class Solution:
    def isIsomorphic(self, s, t) -> bool:
        map_two_strings = {}
        x = ""

        for i in range(len(s)):
            if s[i] not in map_two_strings and t[i] not in map_two_strings.values():
                map_two_strings[s[i]] = t[i]
        
        print(map_two_strings)
        print(map_two_strings.values())
        
        for i in range(len(s)):
            if s[i] in map_two_strings:
                x = x + map_two_strings[s[i]]
        
        print(x)

        if x == t:
            return True
        
        return False
        


# s = "egg" 
# t = "add"
# s = "foo"
# t = "bar"
# s = "paper"
# t = "title"
s = "badc"
t = "baba"


print(Solution().isIsomorphic(s, t))