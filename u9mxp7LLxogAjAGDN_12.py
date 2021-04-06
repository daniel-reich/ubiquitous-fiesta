
def factor_sort(nums):
  lst, lst2 = [], []
  for x in nums:
    c = 0
    for i in range (1,x+1):
      if(x%i == 0):
        c += 1
    lst.append([c,x])
  lst.sort()
  lst.reverse()
  for j in lst:
    lst2.append(j[1])
  return lst2

