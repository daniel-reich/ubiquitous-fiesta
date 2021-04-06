
def esthetic(num):
  def isesth(num, x):
    import numpy as np
    num = np.base_repr(num, base=x)
    return all(abs(int(num[i]) - int(num[i - 1])) == 1 for i in range(1, len(num)))
  lst = [x for x in range(2, 11) if isesth(num, x)]
  return lst if lst else 'Anti-Esthetic'

