
def max_possible(n1, n2):
  n2 = sorted(str(n2))
  return int(''.join(\
    [x if n2 == [] or x >= n2[-1] else n2.pop() for x in str(n1)]))

