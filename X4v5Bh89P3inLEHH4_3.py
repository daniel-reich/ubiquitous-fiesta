
def spin_around(lst):
  angle = 0
  for i in lst:
    if i == "right":
      angle+=90
    elif i == "left":
      angle-=90
  absangle = abs(angle)
  turns = absangle/360
  print (int(turns))
  return int(turns)

