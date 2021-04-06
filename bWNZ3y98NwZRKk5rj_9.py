
def block_player(*dots):
  field = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
  ]
  a, b = [[x%3, x//3] if x != 0 else [0, 0] for x in dots]
  x, y = [a if a == b else 3 - (a+b) for a, b in zip(a, b)]
  return field[y][x]

