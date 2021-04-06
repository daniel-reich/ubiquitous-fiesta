
def printgrid(rows, cols):
  
  answer = []
  start = 1
  
  rows_added = 0
  rows_required = rows
  
  while (rows_added < rows_required):
  
    batch = []
    value = start
    columns_added = 0
    columns_required = cols
    
    while (columns_added < columns_required):
      batch.append(value)
      value += rows
      columns_added += 1
    
    answer.append(batch)
    start += 1
    rows_added += 1
  
  return answer

