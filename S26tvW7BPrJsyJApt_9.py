
def next_in_line(lst, num):
  lst.append(num)
  lst.pop(0)
  if len(lst)==0:
    return "No list has been selected"
  return lst

