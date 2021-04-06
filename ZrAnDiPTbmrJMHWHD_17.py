
def is_central(txt):
  le = len(txt) - 1
  if le % 2 != 0:
    return False
  if txt[int(le / 2)] != " ":
    return True
  return False

