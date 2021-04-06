
def can_alternate(s):
  a = s.count("0")
  b = s.count("1")
  
  if a > b+1 or b > a+1:
    return False
  return True

