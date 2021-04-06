
def sim_prop_frac(max_den):
  s = 0
  s_check = set()
  for j in range(1, max_den + 1):
    for i in range(1, j):
      if eval(str(i) + '/' + str(j)) not in s_check:
        s += 1
      s_check.add(eval(str(i) + '/' + str(j)))
  return s

