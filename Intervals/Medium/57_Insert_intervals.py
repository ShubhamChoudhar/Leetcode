class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        temp = []
        i = 1
        while i < len(intervals):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                temp.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            i += 1

        temp.append([start, end])

        return temp

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval))