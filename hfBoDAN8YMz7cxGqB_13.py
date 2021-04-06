
def we_have_house(hh, hw, hd, rh):
    if rh + hh > 20:
        return "No permission."
    if max(hw, hd) > 44:
        return "House too big."
    if 1 + 4 + 1 + 3 + 1 + 4 + 1 > hw:
        # front too small
        return "House too small."
    if 1 + 4 + 1 + 4 + 1 > hd:
        # side too small
        return "House too small."
    if hh < 8:
        return "House too small."
    # if we reach this point, the house dimensions are OK
    gray = 2 * 2 * (hw + hd) - 3 * 2
    yellow = 2 * (hh - 2) * hd - 4 * 4 * 3        # side walls
    yellow += (hh - 2) * hw - 2 * 4 * 3           # back wall
    yellow += (hh - 2) * hw - 2 * 4 * 3 - 5 * 3   # front wall
    if rh > 0:
        # there's not a flat roof:
        yellow += rh * hw
    return "Yellow: " + str(yellow) + ", Gray: " + str(gray)

