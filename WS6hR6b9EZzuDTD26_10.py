
from collections import Counter
def no_duplicate_letters(phrase):
  lst = phrase.split(" ")
  
  for word in lst:
    a = Counter([char for char in word])
    for key in list(a.keys()):
      if a[key] > 1:
        return False
  
  return True

