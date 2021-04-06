
def is_palindrome_possible(txt):
  l = list(txt)
  true = 0
  for a in l:
    if l.count(a) % 2 == 0:
      true = true + 1
  return True if (true == len(l) - 1 and len(l) % 2 == 1) or (true == len(l) and len(l) % 2 == 0) else False

