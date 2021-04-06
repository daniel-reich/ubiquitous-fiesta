
def we_have_house(hh, hw, hd, rh):
  if hh+rh > 20: return "No permission."
  if hw<15 or hd<11: return "House too small."
  if hw>44 or hd>44: return "House too big."
  
  G = str(4*(hw+hd) - 6)
  Y = str(2*(hh-2)*(hw+hd) + rh*hw - 15 - 8*12)
  return "Yellow: {}, Gray: {}".format(Y,G)

