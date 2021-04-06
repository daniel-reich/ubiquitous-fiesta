
def title_to_number(s):
  al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  ans = 0
  for l in s:
    ans = ans*26 + al.index(l)+1
  
  return ans

