
def delete_occurrences(lst, num):
  a = []
  for i in lst:
    if(a.count(i) < num):
      a.append(i)
  return a

