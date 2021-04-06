
def we_have_house(hh, hw, hd, rh): 
    if hh + rh > 20: return 'No permission.'
    if hw > 44 or hd > 44: return 'House too big.' 
    if hw < 15 or hh < 8 or hd < 11: return 'House too small.' 
    grey = 4*(hw+hd) - 6 
    yellow = hw*rh + 2*hh*(hw+hd) - (8*12+21) - grey
    return 'Yellow: {}, Gray: {}'.format(yellow, grey)

