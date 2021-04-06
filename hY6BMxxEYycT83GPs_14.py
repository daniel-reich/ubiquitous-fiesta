
def multiply_by_11(n):
  n = n[::-1]
  ans = ''
  carry = 0
  
  for a,b in zip(n+'0','0'+n):
    carry,nex = divmod(int(a)+int(b)+carry, 10)
    ans+=str(nex)
  
  if carry:
    ans += '1'
  
  return ans[::-1]

