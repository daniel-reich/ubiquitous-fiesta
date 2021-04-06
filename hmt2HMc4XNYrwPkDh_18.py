
def invert_case(c):
  if (c.islower()):
    return c.upper()
  return c.lower()
  
​
def invert(s):
  # your recursive solution here
  if (len(s) == 1):
    return invert_case(s)
    
  return invert(s[1:]) + invert_case(s[0])

