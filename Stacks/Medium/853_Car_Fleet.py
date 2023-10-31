class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_map = []
        time = []

        if len(position) == 1:
            return 1
        
        for index, pos in enumerate(position):
            pos_map.append([pos, speed[index]])
        
        pos_map.sort()
        
        
        for i in range(len(pos_map) - 1, -1, -1):
            print(pos_map[i])
            timeRequired = (target - pos_map[i][0]) / pos_map[i][1]
            if len(time) == 0:
                time.append([pos_map[i][0], timeRequired])
            elif time[-1][1] < timeRequired:
                time.append([pos_map[i][0], timeRequired])
            else:
                pass
        
        return(len(time))


# target = 12
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]

# target = 10
# position = [3]
# speed = [3]

# target = 100
# position = [0,2,4]
# speed = [4,2,1]

# target = 10
# position = [5, 9]
# speed = [5, 1]

target = 10
position = [6, 8]
speed = [3, 2]

print(Solution().carFleet(target, position, speed))