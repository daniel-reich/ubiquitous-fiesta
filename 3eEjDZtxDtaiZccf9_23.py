
def can_play(hand, face):
  y=hand
  z=face
  #splittingthefaceandsavingaslistintext
  text=(z.split())
  #joiningthefaceandthensplittingintolist
  joining= ' '.join(y)
  
  splittinglist=(joining.split())
  
   
 
  
  
​
  
  
  if text[0] in splittinglist or text[1] in splittinglist:
    return True
  else:
    return False

