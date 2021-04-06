
def validations(hh, hw, hd, rh):
  maxHeight = 20
  if (hh + rh) > maxHeight :
    return "No permission."
  landwidth = 50 
  pathwaySize = 3
  if (hw + (2 * pathwaySize)) > landwidth \
    or (hd + (2 * pathwaySize)) > landwidth:
    return "House too big."
  windowWidth = 4
  if ((2 * windowWidth) + 3) > hd  \
    or (3 + (3 * windowWidth))  > hw  \
    or 8 > hh : 
    return "House too small."
  return ""
  
def we_have_house(hh, hw, hd, rh):
  error = validations(hh, hw, hd, rh)
  if error != "" :
    return error
  trimArea = (2 * 2 * hw) + (2 * 2 * hd) - (2*3)
  windowArea = (8 * 4 * 3)  
  doorArea =  7 * 3
  TotalHouseArea = (2 * hh * hw) + (2 * hh * hd) + (2 * 0.5 * hw * rh)
  yellowArea = TotalHouseArea - trimArea - windowArea - doorArea
  return "Yellow: " + str(int(yellowArea)) + ", Gray: " + str(trimArea)

