
def crop_hydrated(field):
  field2 = []
  for r in range(len(field)):
    for c in range(len(field[0])):
      watered = False
      for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
          x = min(max(0, r+i), len(field)-1)
          y = min(max(0, c+j), len(field[0])-1)
          if field[x][y] == 'w':
            watered = True
      field2 += [watered]
  return all(field2)

