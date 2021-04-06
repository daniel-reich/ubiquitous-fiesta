
def bridge_shuffle(list1, list2):
  list3=[]
  for i in range (len(max(list1,list2,key=len))):
    if i>=(len(min(list1,list2,key=len))):
      list3.append(max(list1,list2,key=len)[i])
    else:
      list3.extend((list1[i],list2[i]))
  return list3

