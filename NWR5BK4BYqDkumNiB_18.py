
def digital_division(n):
  c = 0
  if all([n%int(i) == 0 for i in str(n) if int(i) != 0]):
    c += 1
  if n%(sum([int(i) for i in str(n)])) == 0:
    c += 1
  p = 1
  for i in str(n):
    p *= int(i)
  if p != 0 and n%p == 0:
    c += 1
  return "Perfect" if c == 3 else c if c else "Indivisible"

