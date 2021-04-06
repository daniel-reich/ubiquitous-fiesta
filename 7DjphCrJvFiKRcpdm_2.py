
def covered_integers(lst):
  integers = set()
  for a, b in lst:
    integers |= set(range(a, b+1))
  return len(integers)

