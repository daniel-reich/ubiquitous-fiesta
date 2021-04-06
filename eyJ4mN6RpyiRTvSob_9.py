
def is_palindrome_possible(txt):
  odds = [c for c in txt if txt.count(c) % 2 != 0]
  if len(odds) > 1:
    return False
  return True

