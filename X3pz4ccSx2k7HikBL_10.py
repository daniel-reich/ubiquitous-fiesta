
def showdown(p1, p2):
  time1 = p1.index("B")
  time2 = p2.index("B")
  print(time1)
  print(time2)
  if time1 < time2:
    return("p1")
  else:
    if time1 > time2:
      return("p2")
    else:
      if time1 == time2:
        return("tie")

