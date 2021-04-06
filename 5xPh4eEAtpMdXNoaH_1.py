
from collections import Counter
def longest_palindrome(s):
  c = Counter(s)
  return sum(l-l%2 for l in c.values()) + any(l%2 for l in c.values())

