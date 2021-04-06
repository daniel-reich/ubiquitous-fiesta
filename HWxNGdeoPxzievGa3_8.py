
def is_strange_pair(a, b):
  if len(a)>0 and len(b)>0:
    return (a[0]==b[-1])and (a[-1]==b[0])
  elif a == b:
    return True
  return False

