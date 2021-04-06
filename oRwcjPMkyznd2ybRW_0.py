
def max_product(n):
  mx = 0
  ans = []
  for i in range(n + 1):
    prod = 1
    temp = [int(x) for x in str(i)]
    for x in temp:
      prod *= x
    if prod > mx:
      mx = prod
      ans = []
    if prod == mx:
      ans.append(i)
  return ans

