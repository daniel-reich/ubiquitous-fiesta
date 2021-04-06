
def coloured_triangle(row):
  color = ('R','G','B')
  while len(row) > 1:
    row = [a if a==b else next(x for x in color if x!=a and x!=b) for a,b in zip(row,row[1:])]
  return row[0]

