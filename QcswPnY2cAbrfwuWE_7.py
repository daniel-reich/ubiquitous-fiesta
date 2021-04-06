
def filter_factorials(numbers):
  res = [1]
  i = 2
  while res[-1] < max(numbers):
    res.append(i*res[-1])
    i += 1
  return [n for n in numbers if n in res]

