
def longest_palindrome(s):
  c = sum(s.count(x) - [0, 1][s.count(x) % 2] for x in set(s))
  return c + (0 if c == len(s) else 1)

