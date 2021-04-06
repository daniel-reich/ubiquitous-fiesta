
def automorphic(n):
  squaredNumber = n * n
  strSquaredNumber = str(squaredNumber)
  stringNumber = str(n)
  if strSquaredNumber.endswith(stringNumber):
    return True
  return False

