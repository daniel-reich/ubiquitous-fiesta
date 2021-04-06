
def coins_combinations(money, coins):
    m = len(coins)
    table = [[0 for x in range(m)] for x in range(money+1)]
​
    for i in range(m):
        table[0][i] = 1
​
    for i in range(1, money+1):
        for j in range(m):
            x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
​
    return table[money][m-1]

