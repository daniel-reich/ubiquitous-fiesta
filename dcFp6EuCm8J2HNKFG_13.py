
def func(lst,all=0):
  liczba = len(lst)
  if(liczba!=0):
    for m in lst:
      all+=1
      if str(type(m)) == "<class 'list'>":
        all = func(m,all)
    return(all)
  else:
    return(all)

