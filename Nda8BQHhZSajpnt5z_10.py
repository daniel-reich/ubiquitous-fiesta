
def GCD(lst):
  for i in range(min(lst), 0, -1):
    if all([c % i == 0 for c in lst]):
      return i

