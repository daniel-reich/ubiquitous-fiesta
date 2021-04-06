
def cycle_length(lst, n,c=0):
  x=sorted(lst)
  tid=x.index(n)
  nid=lst.index(n)
  if tid==nid:return c
  else:
    mem=lst[x.index(n)]
    minid,maxid=min(tid,nid),max(tid,nid)
    lst=lst[:minid]+[lst[maxid]]+lst[minid+1:maxid]+[lst[minid]]+lst[maxid+1:]
    return cycle_length(lst,mem,c+1)

