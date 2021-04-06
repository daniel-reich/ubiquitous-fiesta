
def left_slide(row):
  i = 0
  count = 0
  while i < len(row) and count < len(row):
    if row[i] == 0:
      del row[i]
      row += [0]
    else:
      i += 1
    count += 1
    
  i = 0
  while i < len(row)-1:
    if row[i] == row[i+1]:
      row[i] = 2*row[i]
      del row[i+1]
      row += [0]
    i += 1
    
  return row

