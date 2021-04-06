
def balanced(lst):
  beg, end = lst[:len(lst)//2], lst[len(lst)//2:]
  return lst if sum(beg)==sum(end) else max((beg,end),key=sum)*2

