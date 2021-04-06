
def XO(txt):
    xtot = 0
    otot = 0
    for all in txt:
        if (all == 'x' or all == 'X'):
            xtot +=1
        if (all == 'o' or all == 'O'):
            otot +=1
    if (xtot == otot):
        return True
    else:
        return False

