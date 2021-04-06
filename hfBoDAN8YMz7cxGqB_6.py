
def we_have_house(hh, hw, hd, rh):
  if(hh+rh>20):
    return "No permission."
  if(hw>44 or hd >44):
    return "House too big."
  if (hh<8 or hw< 15 or hd < 11):
    return "House too small."
  dw = 3 #door width
  
  #Grey paint area: assume for now windows don't enter grey area
  grey_area = 2*(2*hw) + 2*(hd*2) -2*3
  
  #Yellow area
  #Upper
  y1 = hw*rh
  #main wall area
  y2 = 2*hw*(hh-2) + 2*(hd*(hh-2)) 
  #window area
  wa = 4*3*8
  #door area
  da = (7-2)*3
  y2 = y2 - wa - da
  return "Yellow: %i, Gray: %i"%(y1+y2,grey_area)

