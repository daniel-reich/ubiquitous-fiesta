
def major_sum(lst):
  pos=sum([x for x in lst if x>0])
  neg=sum([x for x in lst if x<0])
  return sorted([pos,neg,lst.count(0)], key=abs)[-1]

