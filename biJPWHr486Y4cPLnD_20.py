
def chunkify(lst, size):
  list1=[]
  a=len(lst)//size
  for i in range(1,a+1):
    list1.append(lst[(i-1)*size : i*size])
  if a*size==len(lst):
    return list1
  else:
    list1.append(lst[a*size:])
    return list1

