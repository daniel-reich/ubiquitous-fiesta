
def find_fulcrum(lst):
  
  Fulcrum = 1
  Length = len(lst)
  
  while (Fulcrum < Length):
    
    Left_End = Fulcrum
    Right_Start = Fulcrum + 1
  
    Left_Side = sum(lst[0:Left_End])
    Right_Side = sum(lst[Right_Start:])
    
    if (Left_Side == Right_Side):
      return lst[Fulcrum]
    else:
      Fulcrum += 1
  
  return -1

