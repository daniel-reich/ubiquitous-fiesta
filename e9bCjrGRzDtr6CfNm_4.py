
def solve(a, b):
  try: return round(((3*a)-b-4 )/(b-a) , 3) 
  except: pass
  if (3*a)-b-4 == (b-a):
    return "Any number"
  return "No solution"

