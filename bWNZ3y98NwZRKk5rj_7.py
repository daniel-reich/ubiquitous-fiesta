
def block_player(x, y):
  blocks = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7],
            [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
  for b in blocks:
    if x in b and y in b: return [k for k in b if k not in [x, y]].pop()

