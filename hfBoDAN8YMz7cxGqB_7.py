
def we_have_house(hh, hw, hd, rh):
  if hh+rh>20:return "No permission."
  if hw>44 or hd>44:return "House too big."
  if hw<15 or hd<11 or hh<7:return "House too small."
  gray=4*hd+4*hw-6
  yellow=2*hd*hh+2*hw*hh+rh*hw-96-gray-21
  return "Yellow: "+str(yellow)+", Gray: "+str(gray)

