
def lost_dog(*args):
  l = [("Dog",x+1, y+1) for x in range(len(args)) for y in range(len(args[x]))if args[x][y] == 0]
  return "Dog not found!" if not l else\
  {x[0] + str(i+1): "House ({}) and Room ({})".format(x[1],x[2]) for i,x in enumerate(l)}

