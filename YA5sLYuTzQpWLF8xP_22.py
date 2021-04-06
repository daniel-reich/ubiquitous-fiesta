
def clean_up_list(lst):
  res=[[],[]]
  for x in lst:
    if int(x)%2==0:
      res[0].append(int(x))
    else:
      res[1].append(int(x))
  return res

