
def order(lst):
  return [y for x,y in sorted([(x,y) for y,x in enumerate(lst)])]

