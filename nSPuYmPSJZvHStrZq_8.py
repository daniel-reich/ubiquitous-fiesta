
def oddeven(lst):
  return sum(1 for i in lst if i%2==1)>sum(1 for i in lst if i%2==0)

