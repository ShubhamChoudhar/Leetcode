arr = [14, 13, 6, 19, 27, 43, 7, 8, 1, 2, 10]
# arr1 = [2]
target = 3

# {
#     14: 14,
#     13: 15,
#     6: 22,
#     27: 1,
#     7: 21,
#     1: 27
# }

def match(values, target):
    complement = {}
    for i in range(len(values)):
        if len(complement) > 0 and (values[i] in complement.values()):
            return [ values[i], target-values[i]]
        complement[values[i]] = target - values[i]
    return "No Match!!!"



def match_pairs(values, target):
    for num in values:
        if num < target:
            if (target - num) in values:
                return(num, (target - num))
                
    return("No matching pairs")

def find_pairs(values, target):
    value_dict = {}
    for value in values:
        if (value < target):
            value_dict[value] = value
    for value in value_dict:
        target_compliment = target - value
        if target_compliment in value_dict:
            return (value, target_compliment)
    
    return "No matching pairs"

# print(find_pairs(arr, target))
# print(match_pairs(arr, target))

print(match(arr, target))