
def delete_occurrences(lst, num):
  lst1=[]
  for i in lst:
    if lst1.count(i)<num:
      lst1.append(i)
  return lst1

