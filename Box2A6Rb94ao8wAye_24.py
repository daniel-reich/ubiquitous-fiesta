
def leader(x):
  arr = []
  for i in range(len(x)):
    if x[i] ==  max(x[i:]):
      arr.append(x[i])
  return arr

