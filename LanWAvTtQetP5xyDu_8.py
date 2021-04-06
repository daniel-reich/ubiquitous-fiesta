
def coins_div(lst):
    amount = sum(lst)/3
    for index, coin in enumerate(lst):
        lst.pop(index)
        result = child(coin, lst.copy(), 1, amount)
        lst.insert(index, coin)
        if result:
            return True
    return False
​
​
def child(coins, lst, child_nr, amount):
    if child_nr == 3 and coins == amount:
        return True
    if not lst:
        return False
    if coins < amount:
        for index, coin in enumerate(lst):
            lst.pop(index)
            result = child(coins + coin, lst.copy(), child_nr, amount)
            lst.insert(index, coin)
            if result:
                return True
    elif coins == amount:
        coins = 0
        for index, coin in enumerate(lst):
            lst.pop(index)
            result = child(coins + coin, lst.copy(), child_nr+1, amount)
            lst.insert(index, coin)
            if result:
                return True
    return False

