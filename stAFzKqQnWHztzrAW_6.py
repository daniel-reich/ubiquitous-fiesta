
def add_nums(nums):
  d=[]
  x=nums.split(', ')
  for i in x:
    y=int(i)
    d.append(y)
  return sum(d)

