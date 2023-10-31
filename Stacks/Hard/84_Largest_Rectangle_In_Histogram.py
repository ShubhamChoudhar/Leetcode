class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        result_area = []
        max_area = 0

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        
        for index, height in enumerate(heights):
            start = index
            while result_area[-1][1] > height:
                i, h = result_area.pop()
                max_area = max(max_area, h * (index - i))
                start = i
            result_area.append((start, height))

        for index, height in result_area:
            max_area = max(max_area, height * (len(heights) - index))
        
        return max_area



heights = [2,1,5,6,2,3]
# heights = [2,4]
print(Solution().largestRectangleArea(heights))

# result_area stack hai jiske andar index aur height save kar rahe hai. Agar stack ka last value bada hai aane wale value se toh hum
# area find out karenge aur pop kar denge. start ke variable jisse hum popped index assign kar denge. Aur phir last mai aane wale value
# ko append karenge. Joh stack mai values rahenge uska bhi hum area find out karenge. max function use kiya taaki joh bhi maximum ho
# wohi area ho.
# https://www.youtube.com/watch?v=zx5Sw9130L0&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=4