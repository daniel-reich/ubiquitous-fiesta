
def we_have_house(hh, hw, hd, rh):
  gw = 50
  gd = 50
  if hh + rh > 20:
    return "No permission."
  if gw - 6 < hw or gd - 6 < hd:
    return "House too big."
  if hh < 8 or hw < 15 or hd < 11:
    return "House too small."
  yellow = 2*(hh-2)*hw + 2*(hh-2)*hd + 2*(rh * hw)/2 - 8*4*3 - 3*5
  yellow = int(yellow)
  gray = 2*2*hw + 2*2*hd - 3*2
  return "Yellow: " + str(yellow) + ", Gray: " + str(gray)

