
def larger_than_right(lst):
  return [lst[i] for i in range(len(lst)-1) if lst[i]>max(lst[i+1:])]+[lst[-1]]

