citations = [3,0,6,1,5]
# citations = [2, 2, 2, 2]
# citations = [1,2,1,3]
# citations = [100]
# citations = [11,15]
class Solution:
    def hIndex(self, citations) -> int:
        count = 0
        t = len(citations)
        i = 0
        l = 0
        citations.sort()
        while i in range(len(citations)):
            if citations[i] >= t:
                count += 1
                if count == t:
                    return count
            
            else:
                l -= 1
            
            if l == -1:
                t -= 1
                i = -1
                count = 0
                l = len(citations)  - t
            
            i += 1
        
        return 0
        
        # if t == count:
        #     return count


print(Solution().hIndex(citations))