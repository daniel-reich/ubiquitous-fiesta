
def sum_of_two(a, b, v):
  for i in a:
    if (v - i) in b:
      return True
  return False

