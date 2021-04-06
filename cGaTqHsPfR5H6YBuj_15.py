
def make_sandwich(i,f):
  rturn_list=[]
  for x in i:
    if f not in x:
      rturn_list.append(x)
    else:
      rturn_list.append('bread')
      rturn_list.append(x)
      rturn_list.append('bread')
  return rturn_list

