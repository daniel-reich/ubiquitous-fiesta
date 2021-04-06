
from string import ascii_lowercase
from collections import deque
​
def rolling_cipher(txt, n):
  alphabet = ascii_lowercase
  num = abs(n) if n <= 0 else n*-1
  string = deque(alphabet)
  string.rotate(num)
  return ''.join(string)[:len(txt)]

