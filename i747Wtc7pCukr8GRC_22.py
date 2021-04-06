
def max_product(lst):
  lst=sorted(lst)
  (a,b,c),(x,y,z)=lst[-3:],lst[:2]+lst[-1:]
  return max(a*b*c,x*y*z)
​
def min_product(lst):
  return -max_product(-i for i in lst)

