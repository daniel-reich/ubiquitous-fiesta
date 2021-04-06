
def arithmetic_progression(start, diff, n): 
  arr = [start]
  while len(arr) < n:
    start += diff
    arr.append(start)
  y = str(arr)
  z = y.strip("[ ]")
  return z

