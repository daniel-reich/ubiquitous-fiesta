
def numbers_to_ranges(lst):
  it1,it2,ret = 0,0,[]
  while it2<len(lst):
    if it2<len(lst)-1 and lst[it2]+1==lst[it2+1]:
      it2+=1
    else:
      if it1==it2:
        ret.append(str(lst[it1]))
      else:
        ret.append(str(lst[it1])+'-'+str(lst[it2]))
      it1,it2 = it2+1,it2+1
  return ret

