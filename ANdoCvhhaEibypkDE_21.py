
def closing_in_sum(n):
  if len(str(n))<3: return int(n)
  x = list(map(int,str(n)))
  return 10*x[0]+x[-1]+closing_in_sum(str(n)[1:-1])

