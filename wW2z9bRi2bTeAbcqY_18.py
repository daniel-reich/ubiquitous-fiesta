
def solve(a,b):
  try :
    return round((b-1) / (a-1),3)
  except : 
    if (a-1) == (b-1) == 0:
      return "Any number"
    else : return "No solution"

