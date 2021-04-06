
def next_in_line(lst, num):
  if lst:
    lst.append(num)
    del lst[0]
    return lst
  
  return 'No list has been selected'

