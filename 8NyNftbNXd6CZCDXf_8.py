
def get_coin_balances(lst1, lst2):
  ans=[3,3]
  for i in range(len(lst1)):
    if lst1[i]=='share':
      ans[0]-=1
      ans[1]+=3
    if lst2[i]=='share':
      ans[0]+=3
      ans[1]-=1
  return ans

