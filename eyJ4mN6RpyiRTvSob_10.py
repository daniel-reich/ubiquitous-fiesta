
def is_palindrome_possible(txt):
  return sum(txt.count(c) == 1 for c in txt) <= 1

