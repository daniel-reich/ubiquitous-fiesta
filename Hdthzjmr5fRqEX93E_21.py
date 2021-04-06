
def get_sequence(low, high):
  lst = []
  while low != high + 1:
    lst.append(low)
    low += 1
  return lst

