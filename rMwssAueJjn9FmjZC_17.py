
from collections import Counter
​
​
def number_pairs(txt):
  nums = Counter(txt.split()[1:])
  return sum(value // 2 for value in nums.values())

