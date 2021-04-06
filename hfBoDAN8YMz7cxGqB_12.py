
def we_have_house(hh, hw, hd, rh):
  if hh + rh > 20:
    return "No permission."
  elif hw + 6 > 50 or hd + 6 > 50:
    return "House too big."
  elif hw < 15 or hd < 11:
    return "House too small."
  else:
    grey = (4 * hw + 4 * hd) - 6
    yellow = (2 *(hh * hw) + 2 * (hh * hd)) - grey
    yellow += hw * rh
    yellow -= 117
    return "Yellow: {}, Gray: {}".format(yellow, grey)

