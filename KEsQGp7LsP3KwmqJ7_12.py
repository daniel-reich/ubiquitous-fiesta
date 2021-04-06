
def check(lst):
  y = sum(lst[x]>lst[x-1] for x in range(1,len(lst))) == len(lst)-2
  return 'YES' if y else 'NO'

