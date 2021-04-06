
def count_digits(lst, t):
  o, e = [], []
  for n in lst:
    l = list(str(n))
    odd = [int(x) for x in l if int(x)%2]
    o.append(len(odd))
    ev = [int(x) for x in l if not int(x)%2]
    e.append(len(ev))
  return o if t=='odd' else e

