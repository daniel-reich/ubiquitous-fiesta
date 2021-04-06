
def coins_div(coins):
    '''
    Returns True if coins can be distributed into 3 sets such that each set is
    of equal value.
    '''
    from itertools import combinations
​
    def get_set(coins, target):
        '''
        Helper. Checks through remaining coins to return a coin set which
        adds up to target or returns None if not possible.
        '''
        for i in range(1, len(coins)+1):
            for combo in combinations(coins, i):
                if sum(combo) == target:
                    return combo
​
        return None
    
    coins.sort(reverse=True)
    total = sum(coins)
    target = total // 3
    if total % target != 0:
        return False  # non divisible by 3
​
    for _ in range(3):
        coin_set = get_set(coins, target)
        if not coin_set:
            return False
​
        for coin in coin_set:
            coins.remove(coin)
        
    return True

