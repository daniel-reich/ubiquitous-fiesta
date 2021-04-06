
def coloured_triangle(row):
  if len(row) == 1:
    return row
  elif len(row) > 2:
    return ''.join(sorted(set(row), key=row.index))[-1]
  else:
    return 'R'

