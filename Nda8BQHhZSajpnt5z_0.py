
def GCD(lst):
  for i in range(min(lst), 1, -1):
      if all(not j%i for j in lst):
          return i
  return 1

