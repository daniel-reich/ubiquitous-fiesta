
def smallest(digits, value):
  ans=0
  while len(str(ans))<digits:
    ans+=value
  return ans

