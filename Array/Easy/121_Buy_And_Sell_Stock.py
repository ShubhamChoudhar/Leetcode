# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        temp = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                temp = prices[sell] - prices[buy]
                profit = max(profit, temp)
            
            else:
                buy = sell
                
            sell += 1
            
        return profit

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

print(Solution().maxProfit(prices))

# Intuition:
# We have to find the maximum profit we can make if we buy once and sell in future dates within the array.

# Approach:
# Initiallly, the buy price will be equal to price at 0 index. Sell price will be equal to price at 1 index.
# Profit will be equal to 0 and temp variable to change the profit or difference value. We will iterate through
# the prices array. We will check if prices of buy is lesss than prices of sell. If it is less then we will take
# the difference and max profit and save it to profit variable. If the buy price is greater or equal to sell price
# buy is equal to sell and increment sell by 1. Return profit.
# Time Complexity - O(n)

# Video Link - https://www.youtube.com/watch?v=1pkOgXD63yU
