
def coloured_triangle(row):
  d = {'BG':'R', 'GR':'B', 'BR':'G', 'G':'G', 'R':'R','B':'B'}
  
  while len(row)>1:
    row = ''.join(d[''.join(sorted(set(row[i:i+2])))] for i in range(len(row)-1))
  return row[0]

