
def sum_odd_and_even(lst):
 x=0
 y=0
 for i in lst:
  if i%2==0:
   x=x+i
  else:
   y=y+i
 return [x,y]

