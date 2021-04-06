
def cumulative_sum(lst):
  if len(lst) == 0:
    return []
  nl = [lst[0]]
  cusum = lst[0]
  for i in range(1,len(lst)):
    cusum += lst[i]
    nl.append(cusum)
  return nl

