
def puzzle_pieces(a1, a2):
  if len(a1) != len(a2):
    return False
  return len(set(
    item1 + item2
    for item1, item2
    in zip(a1, a2)
  )) == 1

