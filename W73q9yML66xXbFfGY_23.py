
def coloured_triangle(row):
  if len(row) == 1:
    return row
  
  nex = ''.join(new(a,b) for a,b in zip(row, row[1:]))
  return coloured_triangle(nex)
​
def new(a,b):
  if a==b:
    return a
  for l in 'RGB':
    if l not in [a,b]:
      return l

