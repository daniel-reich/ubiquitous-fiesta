
def next_in_line(lst, num):
  if not lst:
    return 'No list has been selected'
  return lst[1:] + [num]

