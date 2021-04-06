
def islands_perimeter(island):
  island = [[0]*(len(island[0])+2)]+[[0]+i+[0] for i in island]+[[0]*(len(island[0])+2)]
  get_neighbour = lambda y, x: [i for i in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)] if 0 <= i[1] < len(island[0]) and 0 <= i[0] < len(island) and not island[i[0]][i[1]]]
  return len(sum(sum([[get_neighbour(i, j) for j in range(len(island[i])) if island[i][j]] for i in range(len(island))], []), []))

