
def track_robot(instructions):
  x,y=[],[]
  [x.append(int(h[1])) if h[0]=="right" else x.append(-int(h[1])) if h[0]=="left" else y.append(int(h[1])) if h[0]=="up" else y.append(-int(h[1]))  for h in [i.split() for i in instructions]]
  return [sum(x),sum(y)]

