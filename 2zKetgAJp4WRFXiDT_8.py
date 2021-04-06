
def number_length(num):
  ans = 1
  while num>=10:
    num//=10
    ans+=1
  return ans

