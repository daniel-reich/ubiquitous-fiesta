
def we_have_house(hh, hw, hd, rh):
    if hh + rh > 20:
        return "No permission."
    if hw > 44 or hd > 44:
        return "House too big."
    if hw < 15 or hh < 8 or hd < 11:
        return "House too small."
    return "Yellow: %d, Gray: %d" % (rh * hw + (hh - 2) * 2 * (hw + hd) - 111, 4 * (hw + hd) - 6)

