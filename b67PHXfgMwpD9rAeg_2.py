
def plus_sign(txt):
  a = len([txt[i] for i in range(1, len(txt)) if txt[i].isalpha() and txt[i-1] == '+' and txt[i+1] == '+'])
  b = sum([1 for i in txt if i.isalpha()])
  return a == b

