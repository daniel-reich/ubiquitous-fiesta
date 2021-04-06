
from collections import Counter as count
​
def is_full_house(hand):
​
  return sorted(count(hand).values()) == [2, 3]

