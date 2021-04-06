
lead = lambda x: str(int(x))
​
def remove_leading_trailing(n):
  if '.' not in n: return lead(n)
  decimal1 , decimal2 = n.split('.')
  out1, out2 = lead(decimal1), lead(decimal2[::-1])[::-1]
  if out2 != '0':
    return out1 + '.' + out2
  return out1

