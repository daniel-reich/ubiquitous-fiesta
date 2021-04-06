
def sim_prop_frac(max_den):
  lst = []
  total = 0
  for num in range(1, max_den):
    for den in range(num+1, max_den+1):
      if num/den not in lst:
        lst.append(num/den)
        total += 1
  return total

