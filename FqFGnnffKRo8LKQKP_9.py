
def simple_numbers(a, b):
  return [n for n in range(a, b+1) if
      sum(int(x)**y for y, x in enumerate(str(n), start=1)) == n]

