
def pairwise_swap(lst):
  for i in range(len(lst)//2):
    lst[2*i],lst[2*i+1]=lst[2*i+1],lst[2*i]
  if len(lst)%2:  
    k=max(lst, key=lambda y:sum(ord(x) for x in str(y)))
    lst[lst.index(k)], lst[-1]= lst[-1],lst[lst.index(k)]
  return lst

