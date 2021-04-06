
def coins_combinations(money, coins):
    combs = [0] * (money + 1)
    for coin in coins:
        for c in range(money+1):
            if coin == c:
                combs[c] += 1
            if c - coin > 0:
                combs[c] = combs[c] + combs[c - coin]
    return combs[money]

