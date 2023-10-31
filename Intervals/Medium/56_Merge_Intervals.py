class Solution:
    def merge(self, intervals) -> list:
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


intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[0,4]]
print(Solution().merge(intervals))