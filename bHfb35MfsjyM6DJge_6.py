
def route_diff(directions):
  x=0
  y=0
  for s in directions:
    if s=="N": y+=1
    elif s=="S": y-=1
    elif s=="E": x+=1
    else:       x-=1
  return len(directions) -( abs(x) + abs(y) )

