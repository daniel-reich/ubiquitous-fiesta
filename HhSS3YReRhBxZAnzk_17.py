
def gen_values(n, i):
  values = []
  current = 0
  while (round(current,2)) <= n:
    values.append(round(current,2))
    current += i
  return values

