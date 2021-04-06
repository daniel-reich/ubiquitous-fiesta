
def check(lst):
  sort = sorted(lst)
  if sort==lst:
    return 'NO'
  for i in range(len(lst)):
    sort = sort[1:]+sort[:1]
    if sort==lst:
      return 'YES'
  return 'NO'

