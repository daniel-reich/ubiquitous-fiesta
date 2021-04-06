
def get_only_evens(nums):
  newlst = []
  for i,j in enumerate(nums):
    if i % 2 == 0 and j % 2 == 0:
      newlst.append(j)
  return newlst

