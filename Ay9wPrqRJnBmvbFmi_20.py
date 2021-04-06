
def halve_count(a, b):
  i = 0
  while True:
    if a/2 > b:
      a /= 2
      i += 1
    else: 
      break
  return i

