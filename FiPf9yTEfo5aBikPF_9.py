
def coins_combinations(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for denom in coins:
        for a in range(denom, amount+1):
            dp[a] += dp[a-denom]                
    return dp[-1]

