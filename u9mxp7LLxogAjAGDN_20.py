
from operator import itemgetter
def factor_sort(nums):
  temp = []
  nums = sorted(nums,reverse=True)
  for item in nums:
    t = [item]
    ctr = 0
    for j in range(1,item+1):
      if item%j == 0:
        ctr += 1
    t.append(ctr)
    temp.append(t)
  t2 = sorted(temp, key=itemgetter(1),reverse = True)
  result = []
  for i in range(len(t2)):
    result.append(t2[i][0])
  #print(temp)
  return result

