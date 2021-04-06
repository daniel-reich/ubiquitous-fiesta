
def getcalls(fun): 
  outlist = 0
  while callable(fun): 
    outlist += 1
    fun = fun()
  return outlist
def func_sort(lst):
  funlist = [getcalls(i) for i in lst]
  zlist = zip(lst,funlist)
  outlist = sorted(zlist,key = lambda x: x[1])
  outlist = [i[0] for i in outlist]
  return outlist

