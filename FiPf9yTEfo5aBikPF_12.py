
def coins_combinations(money,coins):
    temp = {}
    return combinations(money,coins,len(coins) - 1,temp)
​
def combinations(money,coins,i,temp):
    temp = {}
    if money == 0:
        return 1
    if money < 0 or i < 0:
        return 0
    k = (i,money)
    if k not in temp:
        with_coin = combinations(money - coins[i],coins,i,temp)
        without_coin = combinations(money,coins,i - 1,temp)
        temp[k] = with_coin + without_coin
    return temp[k]

