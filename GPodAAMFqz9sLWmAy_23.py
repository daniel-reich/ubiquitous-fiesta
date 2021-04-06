
def one_odd_one_even(n):
  n = str(n)
  if (int(n[0])+2) % 2 == 0:
    if (int(n[1])+2) % 2 == 1:
      return True
    else:
      return False
  elif (int(n[0])+2) % 2 == 1:
    if (int(n[1])+2) % 2 == 0:
      return True
    else:
      return False

