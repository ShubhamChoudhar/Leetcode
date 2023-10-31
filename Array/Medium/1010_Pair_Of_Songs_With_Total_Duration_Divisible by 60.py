class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        # Approach 1
        # count = 0
        # for i in range(len(time)):
        #     for j in range(i + 1, len(time)):
        #         if(time[i] + time[j]) % 60 == 0:
        #             count += 1
        
        # return count

        # Approach 2
        count = 0
        remainders = {}
        
        for t in time:
            remainder = t % 60
            
            complement = (60 - remainder) % 60
            
            count += remainders.get(complement, 0)

            remainders[remainder] = remainders.get(remainder, 0) + 1

        return count

time = [30,20,150,100,40]
# time = [60,60,60]

print(Solution().numPairsDivisibleBy60(time))