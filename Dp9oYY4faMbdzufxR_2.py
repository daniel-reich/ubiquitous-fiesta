
def left_slide(row):
  length = len(row)
  while 0 in row: del row[row.index(0)]
  for i in range(len(row)-1):
    if row[i] == row[i+1]:
      row[i], row[i+1] =2 * row[i], 0
  while 0 in row: del row[row.index(0)]
  return row + [0] * (length-len(row))

