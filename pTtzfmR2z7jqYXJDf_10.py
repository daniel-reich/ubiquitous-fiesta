
def possible_palindrome(txt):
  return sum(txt.count(c) % 2 for c in set(txt)) <= 1

