
def we_have_house(hh, hw, hd, rh):
  if hw > 44 or hd > 44:
    return "House too big."
​
  if hh + rh > 20:
    return "No permission."
    
  if hd < 11 or hh < 7 or hw < 15:
    return "House too small."
    
  gray = 4 * (hw + hd) - 6
  yellow = 2 * (hh-2) * (hw + hd) + rh * hw - 8 * 12 - 15
  
  return "Yellow: %s, Gray: %s" % (int(yellow), int(gray))

