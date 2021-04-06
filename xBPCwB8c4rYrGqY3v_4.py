
def missing(lst):
  new_lst = [m * 100 for m in lst]
  i = int((new_lst[len(new_lst)-1]-new_lst[0])/len(new_lst))
  new_list = []
  new_list_int = []
  for c in new_lst:
    new_list_int.append(int(c))
  for n in range(new_list_int[0],new_list_int[len(new_list_int)-1],i):
    new_list.append(n)
  for w in new_list:
    if w not in new_list_int:
      if isinstance(lst[0], float):
        return w/100
      else:
        return(int(w/100))

