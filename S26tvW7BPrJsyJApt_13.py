
def next_in_line(lst, num):
  if lst == list(): return "No list has been selected"
  else:
    lst.append(num)
    del(lst[0])
    return lst

