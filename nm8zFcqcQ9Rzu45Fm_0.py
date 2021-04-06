
def bridge_shuffle(lst1, lst2):
  step = 1
  for x in lst2:
    lst1.insert(step,x)
    step += 2
  return lst1

