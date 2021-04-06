
def min_swaps(s):
  alternated = '101010101'
  changes = sum(a != b for a, b in zip(s, alternated))
  return min(changes, len(s) - changes)

