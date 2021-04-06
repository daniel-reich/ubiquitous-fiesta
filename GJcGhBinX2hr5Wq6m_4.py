
def move_zeros(lst):
  lst1=[]
  lst2=[]
  lst3=[]
  for i in lst:
    if i!=0 or i is False:
      lst1.append(i)
    else:
      lst2.append(i)
  lst3=lst1+lst2
  return lst3

