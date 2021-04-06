
from math import ceil
def spartans_cipher(message, n):
  m = ceil(len(message)/ n)
  ret = []
  message = message + " " * (m*n - len(message))
  for i in range(n):
    ret.append(message[:m])
    message = message[m:]
  c = ""
  for i in range(m):
    for j in range(n):
      c += ret[j][i]
  return c.rstrip()

