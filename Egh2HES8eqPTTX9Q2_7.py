
import string
import math
​
def rolling_cipher(txt, n):
  cip = ''
  print(txt)
  for ltr in txt:
    i = 0
    i = string.ascii_lowercase.index(ltr) + n
    i = 26*((i/26) - math.floor(i/26))
    #print(i)
    #print(int(i))
    cip += string.ascii_lowercase[round(i)]
  print(cip)
  return cip

