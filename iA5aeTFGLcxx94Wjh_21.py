
def delete_occurrences(lst, num):
  lst.reverse()
  for el in lst:
    if lst.count(el) > num:
      lst.remove(el)
  lst.reverse()
  return lst

