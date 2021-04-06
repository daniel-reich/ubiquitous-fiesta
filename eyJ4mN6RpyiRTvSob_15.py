
def is_palindrome_possible(txt):
  s = sum(1 for i in txt if txt.count(i) % 2)
  return s == 1 if len(txt) % 2 else not s

