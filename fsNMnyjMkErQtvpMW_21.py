
def holey_sort(lst):
  lst = sorted(lst,key=lambda x: holes(x))
  return lst
  
def holes(num):
  num = str(num)
  ret = 0
  for i in num:
    if i in '4690':
      ret+=1
    elif i=='8':
      ret+=2
  return ret

