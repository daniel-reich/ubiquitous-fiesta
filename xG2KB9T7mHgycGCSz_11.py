
def valid(txt):
  y = []
  for x in txt:
    if not x.isdigit():
      return False
    else:
      y += x
  return len(y) == 4 or len(y) == 6

