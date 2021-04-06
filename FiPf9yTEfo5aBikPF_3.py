
def _coins_combinations(amount, denominations, combinations, *current):
    # if amount is 0 we eneded checking this combination
​
    # DEBUG pprint({'amount': amount, 'current': current_p})
​
    for coin in denominations:
        new_amount = amount - coin
​
        #amount still greater, continue with another
        if new_amount < 0:
            continue
    
        # this variant has come to succesful end, continue
        if new_amount == 0:
            combinations.append(current + (coin,))
            break
​
        # amount still greater than 0, add this coin and continue
        if new_amount > 0:
            valid_denominations = list(filter(lambda x: x >= coin, denominations))
            _coins_combinations(new_amount, valid_denominations, combinations, *current + (coin,))
​
​
def coins_combinations(money, coins):
    combinations = []
    _coins_combinations(money, sorted(coins), combinations,*[])
    return len(combinations)

