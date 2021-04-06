
from string import ascii_lowercase as asc
​
def move(word):
  return ''.join(asc[asc.index(c)+1] for c in word)

