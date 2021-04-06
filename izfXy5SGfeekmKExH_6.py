
def puzzle_pieces(a1, a2):
  return len(set(map(lambda n1, n2: n1+n2, a1, a2))) == 1 if len(a1) == len(a2) else False

