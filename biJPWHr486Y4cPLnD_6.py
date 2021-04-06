
def chunkify(lst, size):
  if len(lst)<size:
    return [lst]
  if len(lst)%size!=0:
    m=size-len(lst)%size
    for i in range(m):
      lst.append(' ')
  result=[]
  for y in range(len(lst)//size):
    for x in range(size):
      if x == 0:
        result.append([])
      result[y].append(lst[x+y*size])
  if result[-1][-1]==' ':
    for i in range(m):
      result[-1].pop()
  return result

