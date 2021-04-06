
from string import ascii_letters as alpha
​
def atbash(txt):
  return txt.translate(str.maketrans(alpha, alpha[::-1].swapcase()))

