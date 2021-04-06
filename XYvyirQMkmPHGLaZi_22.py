
def boom_intensity(n):
  if n>1: ans='B'+'o'*n+'m'
  else: return 'boom'
  if n%5==0: ans=ans.upper()
  if n%2==0: ans+='!'
  return ans

