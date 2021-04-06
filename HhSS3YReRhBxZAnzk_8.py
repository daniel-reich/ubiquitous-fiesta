
def gen_values(n, i):
  number = 0.0
  l = [number]
  while number+i <= n:
    number = round(number+i,2)
    l.append(number)
  return l

