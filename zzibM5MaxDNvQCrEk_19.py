
def will_fit(holds, cargo):
  sum = 0
  for i in holds:
    if i == "S":
      sum += 50
    elif i == "M":
      sum += 100
    else:
      sum += 200
  for i in cargo:
    sum -= i
    if sum < 0:
      return False
  return True

