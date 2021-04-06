
def where_is_waldo(lst):
  for i in lst:
    for j in i:
      if i.count(j)==1:
        return [lst.index(i)+1, i.index(j)+1]

