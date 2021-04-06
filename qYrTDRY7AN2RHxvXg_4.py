
def f(A, c):
  if c**4/4 - A**2*4 >=0:
    return [round((c**2/2 - (c**4/4 - A**2*4)**0.5)**0.5,3),
            round((c**2/2 + (c**4/4 - A**2*4)**0.5)**0.5,3)] 
  else:
    return "Does not exist"

