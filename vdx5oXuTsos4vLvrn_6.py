
def kaprekar_numbers(p, q):
  bla = [str(i) for i in range(p,q+1) if is_kap(i)]
  return ' '.join(bla) if bla else 'INVALID RANGE'
​
def is_kap(n):
  d = len(str(n))
  meh = str(n**2)
  return int(meh[-d:] or '0') + int(meh[:-d] or '0') == n

