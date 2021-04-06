
def accumulating_product(lst):
  ans=1
  new_lst=[]
  for i in lst:
    ans*=i
    new_lst.append(ans)
  return new_lst

