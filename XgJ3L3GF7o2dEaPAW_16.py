
def shared_letters(a, b):
  a = a.lower()
  b = b.lower()
  set_a = set(a)
  set_b = set(b)
  arry = set_a & set_b
  arry = sorted(list(arry))
  string = ''.join(arry)
  return string

