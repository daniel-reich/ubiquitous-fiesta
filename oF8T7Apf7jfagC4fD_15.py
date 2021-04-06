
def antipodes_average(lst):
  result = []
  if len(lst)%2:
    for i in zip(lst[:-len(lst)//2],lst[-1:-len(lst)//2:-1]):
      result += [sum(i)/2]
  else:
    for i in zip(lst[:-len(lst)//2],lst[-1:-len(lst)//2-1:-1]):
      result += [sum(i)/2]
  return result

