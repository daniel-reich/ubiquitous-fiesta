
def safecracker(start, increments):
  lst = [start - increments[0] if start - increments[0] > 0 else 100 + (start - increments[0])]
  lst.append(lst[-1] + increments[1] if lst[-1] + increments[1] < 100 else (lst[-1] + increments[1]) - 100)
  lst.append(lst[-1] - increments[2] if lst[-1] - increments[2] > 0 else 100 + (lst[-1] - increments[2]))
  return lst

