
def mineral_formation(cave):
  
  Stalactites = 0
  Stalagmites = 0
  
  Column = 0
  
  Rows = len(cave)
  Columns = len(cave[0])
  
  while (Column < Columns):
    
    if (cave[0][Column] == 1) and (cave[-1][Column] == 1):
      Stalactites += 1
      Stalagmites += 1
      Column += 1
      
    elif (cave[0][Column] == 0) and (cave[-1][Column] == 1):
      Stalagmites += 1
      Column += 1
      
    elif (cave[0][Column] == 1) and (cave[-1][Column] == 0):
      Stalactites += 1
      Column += 1
    
    else:
      Column += 1
  
  if (Stalactites > 0) and (Stalagmites > 0):
    return "both"
  elif (Stalactites > 0) and (Stalagmites == 0):
    return "stalactites"
  elif (Stalactites == 0) and (Stalagmites > 0):
    return "stalagmites"
  else:
    return "neither"

