
def accumulating_product(lst):
  ans=[]
  prod=1
  for i in range(len(lst)):
    prod*=lst[i]
    ans.append(prod)
  return ans

