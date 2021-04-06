
def split(x):
  div = x//3
  if x < 4:
    return x
  else:
    nums = [3 for i in range(div)]
    diff = x - sum(nums)
    if diff != 0:
      nums[-1] += diff
  if x%30 ==0:
    extra = x//30
  else:
    extra = x//30 + 1
  secret = len(nums)+extra
​
  return round((x/secret)**secret ,1)

