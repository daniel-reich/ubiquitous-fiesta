
def find_a_seat(n, lst):
  half = n / len(lst) / 2
  res = [i for i, j in enumerate(lst) if j <= half]
  
  try:
    return res[0]
  except IndexError:
    return -1

