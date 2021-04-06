
def will_fit(holds, cargo):
  i = 0
  fit = False
  for x in holds:
    if holds[i] == "S":
      if cargo[i] <= 50:
        fit = True
      else:
        fit = False
        break
    if holds[i] == "M":
      if cargo[i] <= 100:
        fit = True
      else:
        fit = False
        break
    if holds[i] == "L":
      if cargo[i] <= 200:
        fit = True
      else:
        fit = False
        break
    i += 1
  return fit

