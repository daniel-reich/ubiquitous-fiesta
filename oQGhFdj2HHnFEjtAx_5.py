
def slicer(string, slic):
  if string==slic:
    return "[:]"
  for x in range(len(string)):
    if string[x]==slic:
      return "["+str(x)+"]"
    for y in range(len(string)):
      if string[:y]==slic:
        return "[:"+str(y)+"]"
      if string[x:y]==slic:
        return "["+str(x)+":"+str(y)+"]"
      for z in range(-len(string),len(string)):
        if z!=0:
          if string[::z]==slic:
            return "[::"+str(z)+"]"
          elif string[x::z]==slic:
            return "["+str(x)+"::"+str(z)+"]"
          elif string[:y:z]==slic:
            return "[:"+str(y)+":"+str(z)+"]"
          elif string[x:y:z]==slic:
            return "["+str(x)+":"+str(y)+":"+str(z)+"]"

