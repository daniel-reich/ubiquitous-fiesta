
import numpy as np
def rps(s1, s2):
  a=np.array([["rock","paper","scissors"],["TIE","Player 2 wins","Player 1 wins"]])
  o=np.where(a[0]==s2)[0][0]-np.where(a[0]==s1)[0][0]
  return a[1][o]

