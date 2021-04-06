
from string import ascii_lowercase as l
​
def get_missing_letters(s):
  return "".join(sorted(set(l).difference(s)))

