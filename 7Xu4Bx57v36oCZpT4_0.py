
def where_is_waldo(lst):
  for row in lst:
    for char in row:
      if row.count(char) == 1:
        return [lst.index(row) + 1, row.index(char) + 1]

