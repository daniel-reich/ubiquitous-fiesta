
def bridge_shuffle(lst1, lst2):
  retList = []
  for idx in zip(lst1, lst2):
    retList.append(idx[0])
    retList.append(idx[1])
  
  if len(lst1) > len(lst2):
    # retList.append(lst1[len(lst2) : ])
    list(map((lambda x: retList.append(x)), lst1[len(lst2) : ]))
  if len(lst2) > len(lst1):
    list(map((lambda x: retList.append(x)), lst2[len(lst1) : ]))
  
  return retList

