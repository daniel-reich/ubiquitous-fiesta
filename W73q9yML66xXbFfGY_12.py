
def changeme(a,b):
  if a == b:
    return a
  if a == 'R':
    if b == 'G':
      return 'B'
    if b == 'B':
      return 'G'
  if a == 'G':
    if b == 'R':
      return 'B'
    if b == 'B':
      return 'R'
  if a == 'B':
    if b == 'G':
      return 'R'
    if b == 'R':
      return 'G'
    
​
def coloured_triangle(row):
  temp = ''
  while len(row) > 1:
    for i in range(len(row)-1):
      temp += changeme(row[i],row[i+1])
    row = temp
    temp = ''
  return row

