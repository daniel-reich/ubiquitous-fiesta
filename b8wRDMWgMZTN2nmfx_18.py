
def equal(a, b, c):
  counter = 0
  if a == b and a != c:
    counter += 2
  elif a == c and a != b:
    counter += 2
  elif b == c and a != b:
    counter += 2
  elif a == b and a == c:
    counter += 3
  return counter

