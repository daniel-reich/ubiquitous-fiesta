
def kaprekar_numbers(p, q):
  out = []
  for i in range(p, q+1):
    l, r = str(i**2)[:len(str(i**2))//2] or 0, str(i**2)[len(str(i**2))//2:] or 0
    if int(l) + int(r) == i:
      out.append(i)
  return ' '.join(map(str, out)) or 'INVALID RANGE'

