
from math import ceil
​
def ordering(key):
  indices = []
​
  for c in sorted(key):
    i = 0
    while True:
      i = key.index(c, i)
      if i not in indices: break
      i += 1
    indices.append(i)
​
  return indices
​
def nico_cipher(message, key):
  x = [[k, []] for k in key]
​
  n = ceil(len(message) / len(key)) * len(key)
  for i in range(n):
    x[i % len(key)][1].append(message[i] if i < len(message) else " ")
​
  order = ordering(key)
  res = ""
  for i in range(n):
    res += x[order[i % len(key)]][1].pop(0)
​
  return res

