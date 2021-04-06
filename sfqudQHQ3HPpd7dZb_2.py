
def rps(p1,p2):
  if p1 == p2:
    return "It's a draw"
  return "The winner is p1" if p1[0] + p2[0] in {'PR','RS','SP'} else "The winner is p2"

