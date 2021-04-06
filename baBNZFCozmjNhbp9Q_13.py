
def box_seq(step):
  steps = {1: lambda n: n + 3, 0: lambda n: n - 1}
  out = 1
  for i in range(step+1):
    out = steps[i%2](out)
  return out

