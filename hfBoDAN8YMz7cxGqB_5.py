
def we_have_house(hh, hw, hd, rh):
    if hh + rh > 20:
        return 'No permission.'
    if hw < 15 or hd < 11:
        return 'House too small.'
    if hw > 44 or hd > 44:
        return 'House too big.'
​
    y = 2 * (hw * hh + .5 * hw * rh) + 2 * (hd * hh)
    y -= 117 + 2 * hw + 2 * (hw-3) + 4 * hd
​
    g = 2 * hw + 2 * (hw-3) + 4 * hd
​
    myans = 'Yellow: ' + str(int(y)) + ', Gray: ' + str(int(g))
​
    return myans

