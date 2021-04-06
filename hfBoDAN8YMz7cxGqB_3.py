
def we_have_house(hh, hw, hd, rh):
  if max(hw,hd) + 6 > 50:
    return "House too big."
  if hw < 15 or hd < 11 or hh < 8:
    return "House too small."
  if hh + rh > 20:
    return "No permission."
  perim = 2 * (hw + hd)
  yellow = (hh - 2) * perim + hw * rh - 111
  gray = (perim - 3) * 2
  return "Yellow: {}, Gray: {}".format(yellow, gray)

