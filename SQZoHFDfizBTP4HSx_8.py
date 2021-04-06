
from string import ascii_lowercase
from collections import Counter
def missing_alphabets (str):
  cnt = Counter(str)
  nb_alpha = max([v for v in cnt.values()])
  return  "".join([char*(nb_alpha - cnt[char]) for char in ascii_lowercase])

