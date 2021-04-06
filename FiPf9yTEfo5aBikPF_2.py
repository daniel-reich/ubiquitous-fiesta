
def coins_combinations(money, coins):
  A=[0]*(money+1)
  A[0]=1
  for x in coins:
    for i in range(money-x+1):
      A[i+x]+=A[i]
  return A[money]

