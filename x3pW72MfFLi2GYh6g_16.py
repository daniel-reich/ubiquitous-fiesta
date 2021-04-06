
def is_scalable(lst):
  return ([lst[0]] + [lst[i] for i in range(1,len(lst)) if lst[i-1]-5 <= lst[i] <= lst[i-1]+5]) == lst

