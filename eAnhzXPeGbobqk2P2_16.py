
def century(year):
  import math
  c = math.floor(year/100)
  if year % 100:
    c+=1
  suffix = ""
  if c == 21:
    suffix = "st"
  else:
    suffix = "th"
  return "%s%s century" % (c, suffix)

