
def percent_filled(box):
  s = "".join(box)
  f = s.count(" ")
  e = s.count("o")
  p = e/(f+e)*100
  return str(round(p)) + "%"

