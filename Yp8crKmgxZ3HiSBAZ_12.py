
def freq_count(lst, el):
  ans=[]
  lvl=0
  listinside=True
  while listinside:
    temp=[]
    listinside=False
    for i in lst:
      if isinstance(i, list):
        temp+=[x for x in i]
        listinside=True
    ans.append([lvl, lst.count(el)])
    lst = temp
    lvl+=1
  return ans

