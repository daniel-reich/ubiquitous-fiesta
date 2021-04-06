
import numpy as np
​
def currently_winning(scores):
  y = []
  yc = []
  o = []
  oc = []
  winning = []
  for i in range(len(scores)):
    if i % 2 == 0:
      y.append(scores[i])
    else:
      o.append(scores[i])
  yc = np.cumsum(y)
  oc = np.cumsum(o)
  for j in range(len(yc)):
    if yc[j] == oc[j]:
      winning.append('T')
    elif yc[j] > oc[j]:
      winning.append('Y')
    else:
      winning.append('O')
  return winning

