
def who_wins_tonight(coins, space, price, size):
    a = coins//price
    b = space//size
    if a>b: return 'Bill'
    if b>a: return 'Will'
    return 'Tie'

