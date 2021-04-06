
def clean_up_list(lst):
  l=[]
  l1=[]
  l2=[]
  for i in lst:
    if int(i)%2==0:
      l.append(int(i))
    else:
      l1.append(int(i))
  l2.append(l)
  l2.append(l1)
  return l2

