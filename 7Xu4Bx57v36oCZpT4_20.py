
def where_is_waldo(lst):
  rest, w_row, w_col = '', 0, 0
  for idx, row in enumerate(lst):
    if len(set(row)) == 1:
      rest = row[0]
    if len(set(row)) == 2:
      w_row = idx
    if rest and w_row:
      break
  for i in range(len(lst[w_row])):
    if lst[w_row][i] != rest:
      w_col = i
      break
  return [w_row + 1, w_col + 1]

