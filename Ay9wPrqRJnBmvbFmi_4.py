
def halve_count(a, b):
  count = -1
  while a > b:
    count += 1
    a /= 2
  return count

