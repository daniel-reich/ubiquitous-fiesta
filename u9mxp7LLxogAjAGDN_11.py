
def factor_sort(nums):
  x = {}
  for num in nums:
    y=[i for i in range(1,num+1) if num%i==0]
    x[num]=len(y)
​
  sort_x = sorted(x.items(), key=lambda x: x[0], reverse=True)
  sort_y = sorted(sort_x, key= lambda x: x[1], reverse=True)     
​
  return [i[0] for i in sort_y]

