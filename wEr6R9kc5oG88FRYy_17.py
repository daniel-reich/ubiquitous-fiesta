
import numpy as np
​
​
def get_frame(w, h, ch):
  if w < 3 or h < 3: return 'invalid'
  frame = np.array([
    [0 for _ in range(w)]
    for _ in range(h)
  ])
  frame[1:-1, 1:-1] += 1
  result = []
  for row in frame:
    new = [''.join(ch if i == 0 else ' ' for i in row)]
    result.append(new)
  return result

