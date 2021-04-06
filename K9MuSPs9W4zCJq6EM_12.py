
def cycle_length(lst, n):
  srtlst = sorted(lst)
  count=0
  index=lst.index(n)
  if n==srtlst[index]: return 0
  while lst[index]!=srtlst[index]:
    old=lst[srtlst.index(lst[index])]
    lst[srtlst.index(lst[index])]=lst[index]
    lst[index]=old
    count+=1
  return count

