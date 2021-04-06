
def tree(h):
  if h==1:  return ["#"]
  return [("#"*x).center(h*2-1) for x in range(1,h*2,2)]

