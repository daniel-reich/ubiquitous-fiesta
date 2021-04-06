
def find_missing(lst):
  if lst==[] or lst is None or lst[0]==[]:return False
  l=sorted(lst,key=lambda x:len(x))
  return [i for i in zip(l,range(len(min(l,key=lambda x:len(x))),len(max(l,key=lambda x:len(x)))+1)) if len(i[0])!=i[1]][0][1]

