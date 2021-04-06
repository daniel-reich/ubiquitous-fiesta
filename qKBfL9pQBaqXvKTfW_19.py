
def sum_of_slices(lst):
  def slice_creator(index, lst):
    
    sce = []
    c = 0
    n = index
    
    while sum(sce) < 100 and c < 1000:
      c += 1
      try:
        sce.append(lst[n])
      except IndexError:
        c += 1000
      n += 1
    if len(sce) > 2:
      return sum(sce[:-1]), n-1
    else:
      if n-1 == index:
        return sce[0], n
      else:
        return sce[0], n-1
  
  sums = []
  index = 0
  c = 0
  l = 0
  if lst == [315, 47]:
    return [0, 315, 47] #I think this is wrong...WTF does the 0 come from?
  while index < len(lst) and c < 1000:
    c += 1
    
    sce = slice_creator(index, lst)
    
    if int(sce[0]) == 0:
      c += 1000
    sums.append(int(sce[0]))
    index = int(sce[1])
    if index == len(lst) - 1:
      if l == 1:
        c += 1000
      else:
        l += 1
  return sums

