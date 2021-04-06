
def we_have_house(hh, hw, hd, rh):
  if hh+rh > 20:
    print("No permission.")
    return "No permission."
  elif (hw+6)>50 or (hd+6)>50:
    print("House too big.")
    return "House too big."
  elif (2*(4+2)+3 > hw) or ((4*2)+3 > hd) or (7+1 > hh+rh):
    print("House too small")
    return "House too small."
  else:
    gray = 2*(hw*2)+2*(hd*2) - (3*2)
    yellow =  (2*hw*(hh-2))+(2*hd*(hh-2))-8*(4*3)-((7-2)*3)+(hw*rh)
    print("Yellow: {}, Gray: {}".format(yellow,gray))
    return "Yellow: {}, Gray: {}".format(yellow,gray)

