
s="S0"
def divisible(arg):
  global s
  if not arg:
    if s=="S1":
      s="S2"
    elif s=="S2":
      s="S1"
    return divisible
  elif arg==1:
    if s=="S0":
      s="S1"
    elif s=="S1":
      s="S0"
    return divisible
  a=s
  s="S0"
  if arg=="state":
    return a
  elif a=="S0":
    return "accept"
  return "reject"

