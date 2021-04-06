
def classify_rug(pattern):
​
  isVerticallySem = True
  isHoriztonallySem = True
  
  for counter in range(0,len(pattern)//2):
    if pattern[counter] != pattern[len(pattern)-counter-1]:
      isHoriztonallySem = False
      
  for row in pattern:
    for counter in range(0,len(row)//2):
      if row[counter] != row[len(row)-counter-1]:
        isVerticallySem = False
        
  if isVerticallySem and isHoriztonallySem:
    return "perfect"
  elif isVerticallySem:
    return "vertically symmetric"
  elif isHoriztonallySem:
    return "horizontally symmetric"
  else:
    return "imperfect"

