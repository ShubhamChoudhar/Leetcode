gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gas = [2,3,4]
# cost = [3,4,3]
# gas = [5,1,2,3,4]
# cost = [4,4,1,5,1]

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        # for i in range(len(gas)):
        #     if gas[i] >= cost[i]:
        #         start = i
        #         end = i
        #         tank = gas[i]
        #         if (len(gas) - 1) > i:
        #             index = i + 1
        #         else:
        #             index = 0
        
                # print("Start: ", start)
                # print("Index: ", index)
                # print("End: ", end)
                # print("Tank: ", tank)
        
        #         while True:
        #             if ((tank - cost[index - 1] + gas[index]) >= cost[index]):
        #                 tank = tank + gas[index] - cost[index - 1]
        #                 print("Tank in loop: ", tank)
                    
        #             else:
        #                 break
                    
        #             index = (index + 1) % len(gas)
        #             # start = index
        #             print("Index in loop:", index)

        #             if index == end and (tank >= cost[index - 1]):
        #                 return start
            
        # return -1

        # Initial checks
        if sum(gas) < sum(cost):
            return -1

        # Initialization
        start_index = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
        # If tank goes negative, reset starting point and tank
            print("Tank:", tank)
            if tank < 0:
                start_index = i + 1
                tank = 0

        return start_index



print(Solution().canCompleteCircuit(gas, cost))