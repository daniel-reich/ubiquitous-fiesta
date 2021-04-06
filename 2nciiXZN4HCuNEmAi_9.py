
def flatten(r):
  for i in range(len(r)):
    if type(r[i]) == list:
      r[i:i+1] = flatten(r[i])
  return r

