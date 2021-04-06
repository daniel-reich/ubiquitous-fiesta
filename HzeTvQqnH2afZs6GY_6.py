
def generate_rug(n, direction):
  rug = [[0]*n for _ in range(n)]
  for rc in range(n):
    for p in range(1, n - rc):
      rug[rc+p][rc] = p
      rug[rc][rc+p] = p
  return rug if direction == 'left' else [row[::-1] for row in rug]

