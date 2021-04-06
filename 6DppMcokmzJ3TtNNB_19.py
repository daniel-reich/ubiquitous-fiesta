
def true_alphabetic(txt):
  a = sorted([x for x in txt if x.isalpha()])
  return ''.join([a.pop(0) if y.isalpha() else y for y in txt])

