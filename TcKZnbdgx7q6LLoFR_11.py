
def collect(s, n):
  return collect2(s,n,[])
def collect2(s, n, res):  
  if len(s) < n:
    res.sort()
    return res
  res.append(s[:n])
  return collect2(s[n:],n, res)

