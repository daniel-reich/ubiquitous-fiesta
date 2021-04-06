
def mark_maths(lst):
  x = 0
  for i in lst:
    i = i.split("=")
    if eval(i[0]) == int(i[1]):
      x+=1
  return str(round(x/len(lst)*100)) + "%"

