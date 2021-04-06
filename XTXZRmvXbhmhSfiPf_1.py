
def single_number(n):
  for x in set(n):
    if n.count(x)==1:return x

