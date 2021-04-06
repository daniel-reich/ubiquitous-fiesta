
def we_have_house(hh, hw, hd, rh):
  if hh + rh > 20: return "No permission."
  if hw > 44 or hd > 44: return "House too big."
  if hh < 8 or hw < 15 or hd < 11: return "House too small."
  
  grey = (2 * 2 * hw) + ( 2 * 2 * hd) - 6
  windowspace = 8 * 3 * 4
  doorspace = 3 * 5 #only for yellow paint, the other 2 feet are subtracted from grey
  yellow = (2 * (hh - 2) * hd) + (2 * (hh - 2) * hw) + (rh * hw) - windowspace - doorspace
  return "Yellow: {}, Gray: {}".format(str(yellow),str(grey))

