
def accumulating_product(lst):
  mul = 1 
  mylist = []
  for i in range (len(lst)):
   mul *= lst[i]
   mylist.append(mul)
  return mylist

