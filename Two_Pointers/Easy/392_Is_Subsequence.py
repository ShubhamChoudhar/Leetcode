s = "agb"
t = "ahbgdc"

def is_subseq(s, t):
    count = 0
    k = 0
    for i in range(len(s)):
        for j in range(k, len(t)):
            if t[j] == s[i]:
                count += 1
                k = j + 1
        
    return count == len(s)

def is_seq(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
        
    return i == len(s)

print(is_subseq(s, t))
print(is_seq(s, t))