
def unique_abbrev(abbs, words):
  x=[i for i in words if i.startswith(abbs[0])]
  y=[i for i in words if i.startswith(abbs[1])]
  z=x=[i for i in words if i.startswith(abbs[2])]
  return  len(x)==1 and len(y)==1 and len(z)==1

