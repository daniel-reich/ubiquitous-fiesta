
from string import ascii_lowercase
​
def add_letters(a):
  alpha = {letter: ord(letter) - ord('a') + 1 for letter in ascii_lowercase}
  value = {v: k for k, v in alpha.items()}
  numeric = sum(map(lambda x: alpha.get(x), a)) % 26
  return value.get(numeric, 'z')

