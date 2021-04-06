
def longest_substring(d):
  s = ""
  m = ""
  for i in range(len(d)-1):
    s+=d[i]
    if int(d[i])%2==int(d[i+1])%2:
      if len(s)>len(m):
        m = s
      s=""
  s+=d[-1]
  if len(s)>len(m):
        m = s
  
  return m

