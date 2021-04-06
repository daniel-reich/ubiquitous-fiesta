
from collections import Counter
def longest_palindrome(s):
  cnt = Counter(s)
  odds = sum(v%2 for v in cnt.values())
  return len(s) - max(0, odds-1)

