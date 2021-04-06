
def century(year):
  import math
  c=(year-1)//100+1
  if c==21:
    return "21st century"
  else:
    return "{}th century".format(c)

