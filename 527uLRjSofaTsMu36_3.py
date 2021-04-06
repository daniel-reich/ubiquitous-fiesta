
import math
​
def get_middle(word):
  m = math.floor(len(word) / 2)
  return word[m-1:m+1] if len(word) % 2 == 0 else word[m]

