
def digital_division(n):
  c1 = all([n % int(i) == 0 for i in str(n) if i != '0'])
  c2 = n % sum(map(int, str(n))) == 0
  c3 = n % eval('*'.join(str(n))) == 0 if '0' not in str(n) else 0
  if all([c1, c2, c3]):
    return "Perfect"
  return sum([c1, c2, c3]) if sum([c1, c2, c3]) != 0 else "Indivisible"

