
def oddeven(lst):
  return sum(i%2 for i in lst) > len(lst)//2

