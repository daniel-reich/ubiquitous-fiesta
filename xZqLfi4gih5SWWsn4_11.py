
def license_plate(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 2):
    Parameters.append(0)
    Parameters.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    Parameters.append("abcdefghijklmnopqrstuvwxyz")
    Parameters.append("0123456789")
    Parameters.append("")
    Parameters.append(Parameters[0])
  
  Original = Parameters[0]
  Required = Parameters[1]
  Added = Parameters[2]
  Uppers = Parameters[3]
  Lowers = Parameters[4]
  Numbers = Parameters[5]
  Answer = Parameters[6]
  Remaining = Parameters[7]
  
  if (Remaining == ""):
    return Answer
  
  elif (Added == Required):
    Answer = "-" + Answer
    Added = 0
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  elif (Remaining[-1] in Uppers):
    Item = Remaining[-1]
    Answer = Item + Answer
    Added += 1
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  elif (Remaining[-1] in Lowers):
    Item = Remaining[-1]
    Answer = Item.upper() + Answer
    Added += 1
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  elif (Remaining[-1] in Numbers):
    Item = Remaining[-1]
    Answer = str(Item) + Answer
    Added += 1
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  else:
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)

