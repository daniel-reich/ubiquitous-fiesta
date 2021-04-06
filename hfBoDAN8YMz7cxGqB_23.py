
def we_have_house(hh, hw, hd, rh):
  if hh+rh>20:
    return "No permission."
  elif hw<=14 or hd<=10:
    return "House too small."
  elif hw>=45 or hd>=45:
    return "House too big."
  else:
    gray = 2*(2*hw+2*hd)-6
    yellow = (hh-2)*(2*hw+2*hd)+rh*hw-3*5-4*2*12
    resp = "Yellow: "+str(yellow)+", Gray: "+str(gray)
    return resp

