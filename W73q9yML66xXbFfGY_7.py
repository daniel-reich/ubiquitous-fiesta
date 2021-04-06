
def coloured_triangle(row):
  if len(row) == 1:
    return row
  newRow = ""
  for i in range(1,len(row)):
    if row[i-1] == row[i]:
      newRow += row[i]
    elif 'R' not in [row[i-1],row[i]]:
      newRow += 'R'
    elif 'G' not in [row[i-1],row[i]]:
      newRow += 'G'
    else:
      newRow += 'B'
  return coloured_triangle(newRow)

