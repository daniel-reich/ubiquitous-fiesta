
def puzzle_pieces(a1, a2):
  if len(a1) - len(a2) != 0: return False
  zipped = list(zip(a1, a2))
  sums = list(map(sum, zipped))
  return all(x == sums[0] for x in sums)

