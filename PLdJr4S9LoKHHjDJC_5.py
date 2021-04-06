
def identify(*cube):
  
  row_size = len(cube)
  col_sizes = [len(cube[n]) for n in range(row_size)]
  
  if len(list(set(col_sizes))) != 1:
    return 'Missing {}'.format((max(col_sizes) - min(col_sizes)) * col_sizes.count(min(col_sizes)))
  elif row_size == col_sizes[0]:
    return 'Full'
  else:
    return 'Non-Full'

