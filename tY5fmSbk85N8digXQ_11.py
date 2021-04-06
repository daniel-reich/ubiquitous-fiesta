
def ones_infection(arr):
  indexOne = []
  
  for i in arr:
    if 1 in i:
      indexOne.extend([x for x,y in enumerate(i) if y == 1])
      for filledOne in range(len(i)):
        i[filledOne] = 1
  
  for j in arr:
    if 1 not in j:
      for mustFilled in range(len(j)):
        if mustFilled in list(set(indexOne)): j[mustFilled] = 1
        
  return arr

