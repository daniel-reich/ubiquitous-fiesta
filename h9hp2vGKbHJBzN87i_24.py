
def partially_hide(a):
  return " ".join([x[0]+"".join("-" for y in x[1:-1])+x[-1] for x in a.split()])

