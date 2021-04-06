
def final_countdown(lst):
  cnt = 0
  retlst = []
  it = 0
  while len(lst)>0 and it<len(lst):
    if lst[it]==1:
      cnt+=1
      retlst.append(lst[:it+1])
      lst=lst[it+1:]
      it=0
    elif len(lst)>it+1 and lst[it]!=lst[it+1]+1:
      lst=lst[it+1:]
      it=0
    else:
      it+=1
  return [cnt,retlst]

