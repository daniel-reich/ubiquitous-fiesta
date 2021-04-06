
def only_5_and_3(n):
  if n == 3 or n == 5:
    return True
  if n < 3:
    return False
  return only_5_and_3(n - 5) or only_5_and_3(n / 3)

