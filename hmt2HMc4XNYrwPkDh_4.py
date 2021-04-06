
def invert(s, i=0):
  if i == len(s) - 1:
    l8r = s[i]
    if l8r.islower() == True:
      return l8r.upper()
    else:
      return l8r.lower()
  else:
    l8r = s[i]
    if l8r.islower() == True:
      cl8r = l8r.upper()
    else:
      cl8r = l8r.lower()
    
    i += 1
    return invert(s,i) + cl8r

