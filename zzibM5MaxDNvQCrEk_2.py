
def will_fit(holds, cargo):
  total = 0
  for letter in holds:
    if letter == "M":
      total += 100
    elif letter == "S":
      total += 50
    else:
      total += 200
  return total > sum(cargo)

