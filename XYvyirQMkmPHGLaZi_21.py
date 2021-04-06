
def boom_intensity(n):
  boomString = "B"
  if n < 2:
    return "boom"
  
  for x in range(n):
    boomString += 'o'
    
  boomString += "m"
  
  if n % 2 == 0:
    boomString += "!"
  
  if n % 5 == 0:
    return boomString.upper()
  else:
    return boomString

