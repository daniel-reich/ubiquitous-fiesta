
def incremental_depth(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Chopped = Parameters[0]
    Parameters.append(Chopped)
    Doll_One = []
    Parameters.append(Doll_One)
    
  Original = Parameters[0]
  Chopped = Parameters[1]
  Doll_One = Parameters[2]
  
  Doll_Two = []
  
  if (Doll_One == []):
    Doll_Two.append(Chopped[-1])
  else:
    Doll_Two.append(Doll_One)
    Doll_Two.insert(0,Chopped[-1])
    
  Chopped = Chopped[0:-1]
  
  if (Chopped == []):
    return Doll_Two
  else:
    return incremental_depth(Original, Chopped, Doll_Two)

