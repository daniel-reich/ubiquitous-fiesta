
def sort_by_last(txt):
  lst0 = txt.split()
  lst1 = []
  lst2 = []
  lst3 = []
  lst4 = []
  for i in lst0:
    lst1.append(i[-1]);
    lst2.append(txt.split().index(i))
  
  for i in range(len(lst1)):
    lst3.append(str(lst1[i])+str(lst2[i]))
  lst3 = sorted(lst3)
  for i in lst3:
    lst4.append(lst0[int(i[1:])])
  return " ". join(lst4)

