
def lcm(a,b):
  i = max(a,b)
  while True:
    if not (i%a or i%b):
      return i
    i += 1

