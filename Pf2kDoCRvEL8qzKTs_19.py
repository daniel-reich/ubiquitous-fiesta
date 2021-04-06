
import numpy as np
def order_people(lst, people):
  if lst[0] * lst[1] >= people:
    a = np.arange(1, lst[0]*lst[1]+1).reshape(lst[0], lst[1])
    b = lst[0]*lst[1] - people
    row = b // lst[1]
    col = b % lst[1]
    if row != 0 and col != 0:
      a[-row-1, -col:] = a[-row:] = 0
    elif row != 0 and col == 0:
      a[-row:] = 0
    elif row == 0 and col != 0:
      a[-row-1, -col:] = 0
    for i in range(lst[0]):
      if i % 2 == 1:
        a[i] = a[i, ::-1]
    return a.tolist()
  else:
    return "overcrowded"

