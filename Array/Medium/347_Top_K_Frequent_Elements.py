# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter
import heapq

nums = [1,1,1,2,2,3], 
k = 2

class Solution:
    def topKFrequent(self, nums, k: int) -> int:
        frequency_map = Counter(nums)  
        min_heap = []

        for num, freq in frequency_map.items():
            heapq.heappush(min_heap, (-freq, num))

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(min_heap)
            result.append(num)

        return result