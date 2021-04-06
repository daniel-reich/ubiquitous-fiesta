
def left_slide(row):
  row.sort(key=lambda x: x is 0)
  
  for i in range(len(row) - 1):
    if row[i] == row[i+1]:
      row[i] *= 2
      row[i+1] = 0
      
  row.sort(key=lambda x: x is 0)
  return row

