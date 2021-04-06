
def puzzle_pieces(a1, a2):
  return len(a1) == len(a2) and len(set(map(sum, zip(a1, a2)))) == 1

