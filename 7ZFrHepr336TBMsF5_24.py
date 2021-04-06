
def percentage_changed(old, new):
  op = int(old[1:])
  np = int(new[1:])
  perc = "decrease" if op>np else "increase"
  x = abs(round(((op-np)/op) *100))
  
  return "{}% {}".format(x, perc)

