
def delete_occurrences(lst, num):
  lst2 = lst[::-1]
  for i in lst:
    if lst2.count(i)>num:
      lst2.remove(i)
  return lst2[::-1]

