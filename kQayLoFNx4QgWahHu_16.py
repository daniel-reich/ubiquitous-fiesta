
def order(lst):
  return [j for _,j in sorted((v,i) for i,v in enumerate(lst))]

