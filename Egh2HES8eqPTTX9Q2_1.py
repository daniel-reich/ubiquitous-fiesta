
import numpy as np
import string
​
def rolling_cipher(txt, n):
  return ''.join(np.roll(list(string.ascii_lowercase), -n)[:4])

