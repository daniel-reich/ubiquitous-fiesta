
def check(d1, d2, k):
  if k not in d1 or k not in d2:
    return "One's empty"
  
  if d1[k] == d2[k]:
    return True
  
  return 'Not the same'

