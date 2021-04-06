
from collections import Counter
​
def possible_palindrome(txt):
  counter = Counter(txt)
  count_1 = 0
  if len(set(txt)) == 1:
    return True
  for ele in counter:
    if counter[ele] == 1:
      count_1 += 1
      if count_1 > 1:
        return False
      continue
    if counter[ele] % 2 == 0:
      continue
    if counter[ele] % 2 != 0:
      return False
  return True

