
def GCD(lst):
  count = 0
  for i in range(lst[-1], 0, -1):
    for j in lst:
      if j % i == 0:
        count += 1
    if count == len(lst): return i
    count = 0

