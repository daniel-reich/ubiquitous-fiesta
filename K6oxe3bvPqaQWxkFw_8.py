
def join_digits(n):
  s = []
  for i in range(1,n+1):
    s.append(str(i))
  return '-'.join(list(''.join(s)))

