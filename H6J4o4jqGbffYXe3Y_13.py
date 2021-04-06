
def relation_lst(lst):
  lst.sort()
  return [(lst[i],lst[j]) for i in range(len(lst)) for j in range(i,len(lst)) ]

