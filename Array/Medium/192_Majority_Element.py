nums = [3, 2, 3]

def maj_ele(nums):
    frequency = {}
    for item in nums:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    print(frequency)
    
    for num in frequency:
        if frequency[num] > int(len(nums) / 2):
            return num

print(maj_ele(nums))