
def we_have_house(hh, hw, hd, rh):
  if hh+rh>20:return "No permission."
  if hw<15 or hd<11:return "House too small."
  if hw>44 or hd>44:return "House too big."
  Yellow=((hh-2)*hd-24)*2+((hh-2)*hw-24)+((hh-2)*hw-24-15)+rh*hw
  Gray=2*hw+2*(hw-3)+4*hd
  return 'Yellow: {}, Gray: {}'.format(Yellow,Gray)

