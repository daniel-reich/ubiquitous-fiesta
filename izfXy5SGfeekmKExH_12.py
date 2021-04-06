
def puzzle_pieces(a1, a2):
  if len(a1) != len(a2):
    return False
  test = a1[0] + a2[0]
  return all(_a1 + a2[i] == test for i, _a1 in enumerate(a1))

