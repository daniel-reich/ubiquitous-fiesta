
def normal_sequence(n):
  mod = n % 8
  if mod == 1 or mod == 5:
    return 0
  elif mod == 0 or mod == 3 or mod == 2:
    return 1
  else:
    return 2

