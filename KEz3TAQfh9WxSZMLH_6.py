
def count_all(txt):
  res = [ 1 if t.isdigit() else 0 for t in txt.replace(' ', '')]
  return {
    "LETTERS": res.count(0),
    "DIGITS": res.count(1)
  }

