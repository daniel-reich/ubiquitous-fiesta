
def sort_it(lst):
  res,nums =[], sorted([lst[i] if type(lst[i])==int else lst[i][0] for i in range(len(lst))])
  for n in nums:
    for l in lst:
      if type(l) == int and l == n: res.insert(nums.index(n),l)
      if type(l) != int and l[0] == n: res.insert(nums.index(n),l)
  return res

