
def is_ladder_safe(lst):
  #The ladder must be at least 5 characters wide
  if min(len(i) for i in lst) < 5 : return False
  
  #Rungs should not be broken (i.e. no gaps)
  if any("#" in i[1:-1] and " " in i[1:-1] for i in lst) : return False
  
  #The ladder mustn't have more than a 2 character gap between rungs.
  temp = ""
  for i in lst :
    if ' ' in i : temp += '0'
    else : temp += '1'
  
  if "000" in temp : return False
  
  #Rungs must be evenly spaced apart.
  if "101" in temp : return False
  if "11" in temp and "1001" in temp : return False
  
  return True

