
def collect(s, n):
  
  l = []
  stri = ''
  
  for num in range(len(s)):
    if len(stri) == n:
      l.append(stri)
      stri = ''
    stri += s[num]
  
  if len(stri) == n:
    l.append(stri)
    
  return sorted(l)

