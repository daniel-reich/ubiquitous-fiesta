
def available_spots(lst, num):
  
  Likes = 0
  
  First = 0
  Second = 1
  Length = len(lst)
  
  while (Second < Length):
    New = num
    Left = lst[First]
    Right = lst[Second]
  
    if (New % 2 != 0) and (Left % 2 != 0) and (Right % 2 == 0):
      Likes += 1
      First += 1
      Second += 1
    
    elif (New % 2 != 0) and (Left % 2 == 0) and (Right % 2 != 0):
      Likes += 1
      First += 1
      Second += 1
    
    elif (New % 2 != 0) and (Left % 2 != 0) and (Right % 2 != 0):
      Likes += 1
      First += 1
      Second += 1
    
    elif (New % 2 == 0) and (Left % 2 == 0) and (Right % 2 != 0):
      Likes += 1
      First += 1
      Second += 1
    
    elif (New % 2 == 0) and (Left % 2 != 0) and (Right % 2 == 0):
      Likes += 1
      First += 1
      Second += 1
    
    elif (New % 2 == 0) and (Left % 2 == 0) and (Right % 2 == 0):
      Likes += 1
      First += 1
      Second += 1
    
    else:
      First += 1
      Second += 1
  
  return Likes

