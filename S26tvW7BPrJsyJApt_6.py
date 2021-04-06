
def next_in_line(lst, num):
  if lst:
    lst.append(num)
    return lst[1:]
  return "No list has been selected"

