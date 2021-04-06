
def coins_combinations(money, coins):
    if not money:
        return 1
    if money < 0 or not coins:
        return 0
    return (coins_combinations(money - coins[0], coins) +
            coins_combinations(money, coins[1:]))

