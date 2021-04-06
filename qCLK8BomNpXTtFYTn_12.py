
def cumulative_sum(lst):
  if len(lst) <= 1:
    return lst
  new = [lst[0]]
  num = lst[0]
  for n in range(1,len(lst)):
    num += lst[n]
    new.append(num)
  return new

