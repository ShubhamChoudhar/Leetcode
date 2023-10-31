class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        maxlength = 0
        maxwidth = 0

        if len(horizontalCuts) == 1:
            length = max((h - horizontalCuts[0]), (horizontalCuts[0] - 0))
            maxlength = length

        else:
            for i in range(len(horizontalCuts)):
                if i == len(horizontalCuts) - 1:
                    length = h - horizontalCuts[i]
                else:
                    length = horizontalCuts[i + 1] - horizontalCuts[i]
                
                maxlength = max(maxlength, length)
        
        if len(verticalCuts) == 1:
            width = max((w - verticalCuts[0]), (verticalCuts[0] - 0))
            maxwidth = width
        
        else:
            for i in range(len(verticalCuts)):
                if i == len(verticalCuts) - 1:
                    width = w - verticalCuts[i]
                else:
                    width = verticalCuts[i + 1] - verticalCuts[i]

                maxwidth = max(maxwidth, width)
        
        return maxlength * maxwidth

# h = 5
# w = 4
# horizontalCuts = [1,2,4]
# verticalCuts = [1,3]

# h = 5
# w = 4
# horizontalCuts = [3,1]
# verticalCuts = [1]

# h = 5
# w = 4
# horizontalCuts = [3]
# verticalCuts = [3]

h = 1000000000
w = 1000000000
horizontalCuts = [2]
verticalCuts = [2]

print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))