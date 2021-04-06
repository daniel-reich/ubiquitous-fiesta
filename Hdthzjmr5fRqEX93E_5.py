
def get_sequence(low, high):
  x = []
  
  if low == high:
    x.append(low)
  else:
    for i in range(high+1-low):
      x.append(i+low)
  return x

