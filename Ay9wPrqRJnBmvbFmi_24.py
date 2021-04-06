
def halve_count(a, b):
  counter = 0
  while a / 2 > b:
    counter += 1
    a = a / 2
  return counter

