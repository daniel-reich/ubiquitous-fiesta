
def simple_numbers(a, b):
  tot = []
​
  for n in range(a, b + 1):
    if n == sum(d ** (i+1) for i, d in enumerate(map(int, str(n)))):
      tot.append(n)
​
  return tot

