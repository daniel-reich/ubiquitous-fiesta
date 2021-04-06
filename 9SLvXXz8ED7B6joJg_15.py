
def lets_meet(distance, va, vb):
  v = va + vb
  hours = distance / v
  h = 0
  while hours >= 1:
    h += 1
    hours -= 1
  minutes = hours * 60
  m = 0
  while minutes >= 1:
    m += 1
    minutes -= 1
  seconds = minutes * 60
  s = 0
  while seconds >= 1:
    s += 1
    seconds -= 1
  return str(h) + "h " + str(m) + "min " + str(s) + "s"

