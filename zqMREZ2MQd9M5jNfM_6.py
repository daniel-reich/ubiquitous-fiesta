
def is_symmetrical(num):
  x = str(num)
  if x[::]==x[-1::-1]:
    return True
  return False

