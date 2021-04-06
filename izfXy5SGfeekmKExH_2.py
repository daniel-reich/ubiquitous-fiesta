
def puzzle_pieces(a1, a2):
  puzzle = [x + y for x, y in zip(a1, a2)]
  
  if len(a1) != len(a2):
    return False
  else:
    return all(i == puzzle[0] for i in puzzle)

