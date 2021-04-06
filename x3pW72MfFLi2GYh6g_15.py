
def is_scalable(lst):
  return all([abs(lst[x]-lst[x-1])<=5 for x in range(1,len(lst))])

