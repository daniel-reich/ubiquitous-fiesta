
def simple_numbers(a, b):
  result = []
  for i in range(a, b + 1):
    if sum(int(n) ** x for x, n in enumerate(str(i), start = 1)) == i:
      result.append(i)
  return result

