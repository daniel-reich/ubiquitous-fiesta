
def simple_numbers(a, b):
  res = []
  for i in range(a, b + 1):
    if i == sum(int(x) ** (j + 1) for j, x in enumerate(str(i))):
      res.append(i)
  return res

