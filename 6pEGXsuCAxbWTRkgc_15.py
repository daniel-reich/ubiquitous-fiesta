
def loves_me(n):
  s = list()
  for x in range(n):
    s.append(['Loves me not','Loves me'][x%2==0])
  s[-1] = s[-1].upper()
  return ', '.join(s)

