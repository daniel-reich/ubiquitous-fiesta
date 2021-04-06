
def has_digit(txt):
  l=[str(c) for c in range(10)]
  if any([t in l for t in txt]):
    return True
  else:
    return False

