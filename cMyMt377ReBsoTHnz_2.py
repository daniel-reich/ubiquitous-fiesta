
def dict_to_list(d):
  length=len(d)
  lst=[]
  for i in range(0,length):
    lst.append(0)
  i=0
  for x in sorted(d):
    lst[i]=(x, d[x])
    i=i+1
  return lst

