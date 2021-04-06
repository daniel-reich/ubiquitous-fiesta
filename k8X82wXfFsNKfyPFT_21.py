
def clone(lst):
  temp = lst
  lst.append([])
  for i in temp:
    lst[-1].append(i)
  lst[-1].pop()
  return lst

