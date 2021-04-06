
def decrypt(s):
  al = 'abcdefghijklmnopqrstuvwxyz'
​
  ans = ''
  idx = 0
  while idx<len(s):
    if idx+2<len(s) and s[idx+2]=='#':
      ans += al[int(s[idx:idx+2])-1]
      idx += 3
    else:
      ans += al[int(s[idx])-1]
      idx += 1
  
  return ans

