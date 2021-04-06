
def get_coin_balances(reds, greens):
    '''
    Returns a list of red's coins and green's coins after updating them with the
    moves in reds and greens.
    '''
    red_sum = green_sum = 3
    update = lambda x, a, b: (a-1,b+3) if x == 'share' and a > 0 else (a, b)
    
    for r, g in zip(reds, greens):
        red_sum, green_sum = update(r, red_sum, green_sum)
        green_sum, red_sum = update(g, green_sum, red_sum)
        
    return [red_sum, green_sum]

