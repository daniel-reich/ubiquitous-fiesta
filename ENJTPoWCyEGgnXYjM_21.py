
def percent_filled(box):
  x = 0
  y = 0
  for i in box:
    x += i.count(" ")
    y += i.count("o")
  return str(int((y/(x+y))*100))+str("%")

