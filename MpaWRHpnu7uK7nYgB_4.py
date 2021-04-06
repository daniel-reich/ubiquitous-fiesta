
def doubleton(n):
  looking_for_double_town = True 
  
  while looking_for_double_town:
    n += 1 
    if len(set(str(n))) == 2:
      return n

