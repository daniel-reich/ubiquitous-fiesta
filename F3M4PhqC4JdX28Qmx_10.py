
def back_to_home(directions):
  N = 0
  S = 0
  W = 0
  E = 0
  for x in directions:
    if x == "N":
      N += 1
    elif x == "S":
      S += 1
    elif x == "W":
      W += 1
    elif x == "E":
      E += 1
  if N == S and W == E:
    return True
  else:
    return False

