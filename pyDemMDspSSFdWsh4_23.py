
from itertools import cycle
​
def digital_decipher(eMessage, key):
  new_key = [int(i) for i in str(key)]
  return ''.join(chr(i - j + 96)  for i, j in zip(eMessage, cycle(new_key)))

