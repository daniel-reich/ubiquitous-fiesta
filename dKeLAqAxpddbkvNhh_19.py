
def group_seats(lst, n):
  count = 0
  pattern = '0' * n
  for row in lst:
    str_row = ''.join(str(i) for i in row)
    while pattern in str_row:
      count += 1
      str_row = str_row.replace(pattern, pattern[:-1])
  return count

