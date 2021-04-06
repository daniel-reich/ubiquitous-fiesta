
def crop_hydrated(field):
  nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for r in range(len(field)):
    for c in range(len(field[0])):
      if field[r][c] == 'c':
        if all(field[r+i][c+j] == 'c' for i, j in nb if 0<=r+i<len(field) and 0<=c+j<len(field[0])):
          return False
  return True

