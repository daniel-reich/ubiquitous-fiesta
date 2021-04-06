
def we_have_house(hh, hw, hd, rh):
  if hw>44 or hd>44:
    return("House too big.")
  if hh+rh >20:
    return("No permission.")
  if hw<15 or hd<11:
    return("House too small.")
  if rh==0:
    y=2*(hd*(hh-2)-2*4*3)+(hw*(hh-2)-2*4*3)+(hw*(hh-2))-2*4*3-5*3
    g=2*(hw+hd)*2-2*3
    return("Yellow: "+str(int(y))+", Gray: "+str(int(g)))
  else:
    y=2*(hd*(hh-2)-2*4*3)+(hw*(hh-2)-2*4*3)+(hw*(hh-2))-2*4*3-5*3+2*(rh*hw/2)
    g=2*(hw+hd)*2-2*3
    return("Yellow: "+str(int(y))+", Gray: "+str(int(g)))

