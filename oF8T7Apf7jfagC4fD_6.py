
def antipodes_average(lst):
  quant = len(lst)
  lst1 = []
  lst2 = []
  lst3 = []
  for i in range(0, quant//2):
    lst1.append(lst[i])
    lst2.append(lst[-1-i])
    lst3.append((lst1[i] + lst2[i])/2)
    
  return lst3

