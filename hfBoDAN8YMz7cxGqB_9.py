
def we_have_house(hh, hw, hd, rh):
​
  # constants
  fWindows = 24 # area of two windows together (2* 4*3)
  gDoor = 6     # door area in the gray area (3*2)
  yDoor = 15    # door area in the yellow area (3*5)
  hGray = 2     # hight of gray area
  hGardenPaths = 6 # 2 times 3 feet for the path around the house
  HouseHighMax = 20
​
  # check higth - door plus 1
  sError = "House too small."
  if (hh < 8):
    return sError
    
  # check if house is to small for the windows and the door 
  # width frontside - door + 2 windows + 4 feet distance
  if hw < (3+8+4):
    return sError   
  
  # width backside - two windows + 3 feet distance
  if hw < (8+3):
    return sError
    
  # width two sides - two windows + 3 feet distance
  if hd < (8+3):
    return sError
    
  
  # check if house is to small for the garden
  if (hw > (50 - hGardenPaths)) or (hd > 50 - hGardenPaths):
    return "House too big."
  
  # check if house is to high
  if (hh + rh) > HouseHighMax:
    return("No permission.")
  
  
  # Frontside low
  flGray = (hw * hGray) - gDoor
  flYellow = (hw * (hh - hGray)) - (fWindows + yDoor)
  
  # Frontside roof
  frYellow = (hw * rh) / 2
  
  # Backside low
  blGray = hw * hGray
  blYellow = (hw * (hh - hGray)) - (fWindows)
​
  # Backside roof
  brYellow = (hw * rh) / 2
  
  # Right Side
  rGray = hd * hGray
  rYello = (hd * (hh - hGray)) - (fWindows)
  
  # Left Side 
  lGray = rGray
  lYellow = rYello
  
  gGray = int(flGray + blGray + lGray + rGray)
  gYellow = int(flYellow + frYellow + blYellow + brYellow + rYello + lYellow)
  return "Yellow: " + str(gYellow) + ", Gray: " + str(gGray)

