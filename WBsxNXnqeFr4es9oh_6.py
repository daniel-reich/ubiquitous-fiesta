
from math import ceil, sqrt
​
def clockwise_cipher(message):
  message = list(message)
  size = ceil(sqrt(len(message)))
  square = [[" "] * size for _ in range(size)]
  j = 0
  k = 4*(size - 2*j - 1) or 1
​
  while k > 0:
    for i in range(k):
      if not message: break
      if i % 4 == 0: y, x = j, i//4 + j
      if i % 4 == 1: y, x = i//4 + j, (size-1) - j
      if i % 4 == 2: y, x = (size-1) - j, (size-1) - (i//4 + j)
      if i % 4 == 3: y, x = (size-1) - (i//4 + j), j
      square[y][x] = message.pop(0)
​
    j += 1
    k = 4*(size - 2*j - 1) or 1
​
  return "".join(map("".join, square))

