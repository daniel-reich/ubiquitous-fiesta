
from random import shuffle
def numbers():
  arr = ['1','2','3','4','5']
  shuffle(arr)
  return int(''.join(arr))

