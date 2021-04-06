
def chunkify(lst, size):
  b = [lst[size*i:size*i+size] for i in range(len(lst)//size)]
  if len(lst)%size: b+=[lst[-(len(lst)%size):]]
  return b

