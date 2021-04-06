
def delete_occurrences(lst, num):
  lst2=[]
  for l in lst:
    if lst2.count(l)<num:
      lst2.append(l)
  return lst2

