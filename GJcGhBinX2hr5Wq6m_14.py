
def move_zeros(lst):
  return [x for x in lst if x!=0 or type(x)==bool]+[x for x in lst if x==0 and type(x)!=bool]

