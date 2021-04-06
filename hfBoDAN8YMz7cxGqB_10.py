
def we_have_house(hh, hw, hd, rh):
  if hh+rh > 20:
    return "No permission."
  elif hw>44 or hd>44:
    return "House too big."
  elif hw<15 or hd<11:
    return "House too small."
  else:
    y_raw = (rh*hw)+2*(hw*hh)+2*(hd*hh)
    gray = 2*(hw*2)+2*(hd*2)-(2*3)
    yellow = y_raw-gray-8*(3*4)-(7*3)
    
    return "Yellow: {}, Gray: {}".format(yellow, gray)

