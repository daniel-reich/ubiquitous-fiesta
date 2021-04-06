
def mumbling(s):
  return "-".join((x*(i+1)).capitalize() for i,x in enumerate(s))

