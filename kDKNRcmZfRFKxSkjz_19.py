
def unmix(txt):
  ans = ''
  for i in range(0,len(txt),2):
    temp = txt[i:i+2]
    ans += temp[::-1]
  return ans

