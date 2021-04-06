
import numpy as np
def bugger(num):
  num = str(num)
  if len(num) == 1:
    return 0
  results = []
  while len(num)> 1:
    results.append(np.prod([int(n) for n in num]))
    num = str(results[-1])
  return len(results)

