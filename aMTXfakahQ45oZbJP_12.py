
def complete_bracelet(lst):
  print(lst)
  for i in range(2, len(lst)//2+1):
    if len(lst)%i == 0:
      iter1 = len(lst)//i
      lst_new = []
      lst_tmp = lst[0:i]
      for j in range(iter1):
        lst_new = lst_new + lst_tmp
      if lst_new == lst:
        return True
  return False

