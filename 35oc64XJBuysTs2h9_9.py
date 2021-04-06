
def get_quartiles(lst, method):
  lst = sorted(lst)
  med = lambda lst: lst[len(lst)//2] if len(lst)%2 else (lst[len(lst)//2]+lst[-1+len(lst)//2])/2
  
  l = len(lst)
  if method == "MS":
    q1 = lst[int(round((l+1.001)/4,0))-1]
    q3 = lst[int(round(3*(l+0.999)/4,0))-1]
  else:
    if method == "T": L,U = lst[:(l+l%2)//2],lst[(l-l%2)//2:]
    if method == "MM": L,U = lst[:(l-l%2)//2],lst[(l+l%2)//2:]
    q1, q3 = med(L), med(U)
  return [lst[0], q1, med(lst), q3, lst[-1]]

