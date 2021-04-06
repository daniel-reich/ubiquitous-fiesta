
def simple_numbers(a, b):
  res = []
  for i in range(a,b+1):
    formula = sum([pow(int(digit), idx+1) for idx,digit in enumerate(str(i))])
    if formula == i:
      res.append(i)
  return res

