n = 31

def count_coins(cents):
    count = 0
    if cents < 1:
        return 0
    while (cents > 0):
        if cents > 25:
            cents = cents - 25
            count += 1
        elif cents > 10:
            cents = cents - 10
            count += 1
        elif cents > 5:
            cents = cents - 5
            count += 1
        else:
            cents = cents - 1
            count += 1

    return count

def num_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 5, 1]
    num_of_coins = 0 
    
    for coin in coins:
        num_of_coins += int(cents / coin)
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins

def min_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 5, 1]
    temp = 0
    num_of_coins = cents
    
    for coin in coins:
        temp = int(cents / coin) + cents % coin
        num_of_coins = min(num_of_coins, temp)
    
    return num_of_coins


print(num_coins(n))

print(count_coins(n))

print(min_coins(n))


