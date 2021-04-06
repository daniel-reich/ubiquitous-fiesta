
def we_have_house(h, w, d, r):
    if w > 44 or d > 44:
        return "House too big."
    if h + r > 20:
        return "No permission."
    if w < 15 or d < 11 or h < 8:
        return "House too small."
    return "Yellow: {}, Gray: {}".format(2*(w+d)*(h-2)+(w*r)-111, 4*(w+d)-6)

