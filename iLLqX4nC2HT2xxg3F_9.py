
def deepest(lst):
  res = []
  for x in lst:
    count = 1
    for y in str(x):
      if y=='[':
        count+=1
      if y==']':
        break
    res.append(count)
  return max(res)

