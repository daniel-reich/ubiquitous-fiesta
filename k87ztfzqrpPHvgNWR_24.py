
def widen_streets(lst, n):
  new_strt = []
  final_str = []
  if len(lst)>1:
    lst.append(' '*len(lst[0]))
    for i in range(len(lst)-1):
      for j in range(len(lst[i])):
        if lst[i][j]==" " and lst[i+1][j]==" ":
          new_strt.append(lst[i][j]*n)
        else:
          new_strt.append(lst[i][j])
      final_str.append("".join(new_strt))
      new_strt.clear()
  else:
    for i in lst:
      final_str.append(i.replace(" "," "*n))
  return final_str

