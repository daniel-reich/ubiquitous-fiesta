
def sums_up(lst):
  FinalPairList = list()
  tmpList =  list()
  for num in lst:
    for i in tmpList:
      if (i+num) == 8:
        pair= []
        if i<num:
          pair.append(i)
          pair.append(num)
        else:
          pair.append(num)
          pair.append(i)
        FinalPairList.append(pair)
    tmpList.append(num)
​
  return{'pairs':FinalPairList }

