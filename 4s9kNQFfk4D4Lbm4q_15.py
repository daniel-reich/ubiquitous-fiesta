
import string 
​
def ABA(s):
  ans = ''
  t = list(string.ascii_uppercase)
  for i in t[0:t.index(s) + 1]:
    ans = ans + i + ans
  return ans

