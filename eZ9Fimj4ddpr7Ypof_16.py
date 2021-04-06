
def mumbling(s):
  return "-".join([x.upper() + x.lower()*y for y,x in enumerate(s)])

