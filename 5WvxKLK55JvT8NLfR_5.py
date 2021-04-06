
import numpy as np
​
def diag_dom(lst):
  D = np.diag(np.abs(lst))
  S = np.sum(np.abs(lst), axis=1) - D
  return all(D > S)

