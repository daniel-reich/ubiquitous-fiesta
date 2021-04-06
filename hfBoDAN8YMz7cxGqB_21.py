
def we_have_house(hh, hw, hd, rh):
    if hh + rh > 20: return 'No permission.'
    if hw>44 or hd>44: return 'House too big.'
    if hw<15 or hd<11: return 'House too small.'
    y = rh*hw + (hw+hd)*(hh-2)*2 - 111
    g = 4*(hw+hd)-6
    return "Yellow: {}, Gray: {}".format(y,g)

