
def esthetic(num):
  lst = []
  for i in range(2, 11):
    s = base(i, num)
    if len(s) == 1 or all(abs(int(a) - int(b)) == 1 for a, b in zip(s, s[1:])):
      lst.append(i)
  return lst or 'Anti-Esthetic'
  
def base(b, n):
  lst = []
  while n > 0:
    lst.append(n % b)
    n //= b
  return ''.join(str(i) for i in lst)

