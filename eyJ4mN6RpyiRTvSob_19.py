
def is_palindrome_possible(txt):
  return sum(txt.count(c) & 1 > 0 for c in set(txt)) < 2

