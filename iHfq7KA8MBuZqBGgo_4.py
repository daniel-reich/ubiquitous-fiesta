
def is_legitimate(lst):
  z=list(map(list,zip(*lst)))
  return sum(lst[0]+lst[-1]+z[0]+z[-1])==0

