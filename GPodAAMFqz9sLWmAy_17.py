
def one_odd_one_even(n):
  a = [int(x) for x in str(n)]
  if a[0] % 2 == 0 and a[1] % 2 != 0:
    return True
  elif  a[1] % 2 == 0 and a[0] % 2 != 0:
    return True
  else:
    return False

