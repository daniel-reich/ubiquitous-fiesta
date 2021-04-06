
def oddeven(lst):
  return [1 for i in lst if i%2==0].count(1) < [1 for i in lst if i%2!=0].count(1)

