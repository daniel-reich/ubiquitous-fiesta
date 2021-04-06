
def next_in_line(lst, num):
  if lst == []:
    return "No list has been selected"
  lst.append(num)
  lst.pop(0)
  return lst

