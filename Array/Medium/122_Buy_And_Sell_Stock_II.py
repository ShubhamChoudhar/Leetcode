class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        last = prices[0]
        for price in prices:
            if price >= last:
                ans += price - last
            last = price
        return ans

prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]

print(Solution().maxProfit(prices))