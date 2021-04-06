
def halve_count(a, b):
  count = 0
  while a / 2 > b:
    a = a / 2
    count += 1
  return count

