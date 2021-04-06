
def expanded_form(num):
  l = len(str(num))
  digits = list(map(int, list(str(num))))
  terms = [d*10**(l-i-1) for i, d in enumerate(digits) if d != 0]
  return ' + '.join(map(str, terms))

