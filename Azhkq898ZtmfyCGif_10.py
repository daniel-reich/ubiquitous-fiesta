
def numbers_to_ranges(lst):
  if(lst == []): return []
  lenLst = len(lst)
  currRange = [str(lst[0]),'-',None]
  rangeList = []
  for i in range(lenLst):
    if(i == lenLst-1):
      if(currRange[2] == None):
        rangeList.append(currRange[0])
      else:
        rangeList.append(currRange[0]+currRange[1]+currRange[2])
    elif(lst[i+1] == lst[i]+1):
      currRange[2] = str(lst[i+1])
    else:
      if(currRange[2] == None):
        rangeList.append(currRange[0])
      else:
        rangeList.append(currRange[0]+currRange[1]+currRange[2])
      currRange = [str(lst[i+1]),'-',None]
  return rangeList

