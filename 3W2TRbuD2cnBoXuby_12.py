
def collect(s, n):
  res =[]
  for i in range(0,len(s),n):
    if(len(s[i:i+n])==n):res.append(s[i:i+n])
  return sorted(res)

