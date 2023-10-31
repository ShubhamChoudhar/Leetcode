class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        min_sum = float('inf')
        window_sum = 0
        
        for i in range(n - k):
            window_sum += cardPoints[i]
            min_sum = min(min_sum, window_sum)
        
        return (total_sum - min_sum)

cardPoints = [1,2,3,4,5,6,1]
k = 3

# cardPoints = [2,2,2]
# k = 2

# cardPoints = [9,7,7,9,7,7,9]
# k = 7

print(Solution().maxScore(cardPoints, k))