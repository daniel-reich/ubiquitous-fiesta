
def coins_combinations(n, coins):
    '''
    Returns the number of ways any number of coins in coins can be combined
    to equal n
    '''
    return helper(coins, len(coins), n)
​
def helper(denoms, num_denoms, n):
    '''
    Computes the number of ways coins in coins can be combined to equal n
    '''
    table = [0 for _ in range(n+1)]
    table[0] = 1  # initialise
​
    for i in range(num_denoms):
        for j in range(denoms[i], n+1):
            table[j] += table[j-denoms[i]]
​
    return table[n]

