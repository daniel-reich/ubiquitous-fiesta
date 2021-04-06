
def get_sequence(low, high):
  lst = [low]
  for i in range(high-low):
    lst.append(i+low+1)
  return lst

