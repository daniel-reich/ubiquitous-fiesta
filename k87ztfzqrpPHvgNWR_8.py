
def widen_streets(lst, n):
  def is_street(lst, column):
    for row in lst:
      if row[column] == '#':
        return False
    return True
  streets = [
    is_street(lst, index)
    for index, column in enumerate(lst[0])
  ]
  result = []
  for row in lst:
    cur_row = []
    for column, street in zip(row, streets):
      if column == ' ' and street:
        cur_row.append(' ' * (n - 1))
      cur_row.append(column)
    result.append(''.join(cur_row))
  return result

