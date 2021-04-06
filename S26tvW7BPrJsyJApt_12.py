
def next_in_line(lst, num):
  if len(lst) == 0:
    return "No list has been selected"
  lst.pop(0)
  lst.append(num)
  return lst

