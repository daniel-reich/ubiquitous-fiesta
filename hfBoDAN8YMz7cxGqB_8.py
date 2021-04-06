
def we_have_house(hh, hw, hd, rh):
    if hw + 6 > 50 or hd + 6 > 50:
        return 'House too big.'
    if hh + rh > 20:
        return 'No permission.'
    if hh < 8 or hw < 15 or hd < 11:
        return 'House too small.'
    widows = 3 * 4 * 2 * 4
    door = 5 * 3
    yellow = (hh - 2) * (hw + hd) * 2 + rh * hw - widows - door
    grey = 2 * (2 * (hw + hd) - 3)
    return 'Yellow: {}, Gray: {}'.format(yellow, grey)

