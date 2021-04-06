
def concatenation_sum(n):
  nl, count = len(str(n)), 0
  for d in range(1, nl):
    count += d * 9 * 10**(d-1)
  count += nl * (n + 1 - 10**(nl-1))
  return count

