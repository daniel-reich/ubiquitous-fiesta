
from collections import Counter
​
def remove_letters(letters, word):
  remaining = (Counter(letters) - Counter(word)).keys()
  return sorted(remaining, key=letters.index)

