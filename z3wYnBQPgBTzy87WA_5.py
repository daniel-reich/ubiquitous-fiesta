
import numpy as np
def rps(s1, s2):
  scores = {'rock':1,'paper':2,'scissors':3}
  t = np.array(['TIE','Player 1 wins','Player 2 wins'])
  return t[scores[s1]-scores[s2]]

