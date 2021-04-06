
def halve_count(a, b):
  count = 0
  while a > b:
    if a/2 > b:
      count += 1
    a /= 2
  return count

