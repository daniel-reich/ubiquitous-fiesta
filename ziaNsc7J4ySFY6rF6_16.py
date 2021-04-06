
def will_fit(holds, cargo):
  n = 0
  for i in holds:
    if i == "S":
      n += 50
    if i == "M":
      n += 100
    if i == "L":
      n += 200
  if n >= sum(cargo):
    return True
  else:
    return False

