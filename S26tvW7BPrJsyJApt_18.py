
def next_in_line(lst, num):
  if not lst:
    return 'No list has been selected'
  else:
    lst.append(num)
    lst.pop(0)
  return lst

