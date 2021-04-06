
import numpy as np
def rps(s1, s2):
  a = np.array(['rock','scissors','paper'])
  if s1 != s2:
    for i in range(len(a)):
      if s1 == a[i]:
        if s2 == a[i-1]:
          return 'Player 2 wins'
        else:
          return 'Player 1 wins'
  else:
    return 'TIE'

