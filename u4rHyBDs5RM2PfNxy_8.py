
def count_ones(lst):
  count = 0
  lt = [[]] #seperating 1 and 0
  co = [] #sum of list containing 1
  for x in lst:
    if x==1:
      lt[-1].append(1)
    else:
      lt.append([])
  for x in lt:
    co.append(sum(x))
  for x in co:
    if x>1:
      count+=1
    
      
  return count

