
def balanced(lst):
  lst1 = []
  lst2 = []
  for i in range(1, (len(lst)//2)+1):
    lst1.append(lst[i-1])
  for x in range((len(lst)//2+1), len(lst)+1):
    lst2.append(lst[x-1])
  if sum(lst2)>sum(lst1):
    return lst2 + lst2
  elif sum(lst1)>sum(lst2):
    return lst1 + lst1
  else:
    return lst

