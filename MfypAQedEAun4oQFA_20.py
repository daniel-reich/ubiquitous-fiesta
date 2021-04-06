
def perrin(n):
  ans=[3,0,2]
  if n<3:return ans[n]
  else:
    for i in range(3,n+1):
      ans.append(ans[-2]+ans[-3])
  return ans[-1]

