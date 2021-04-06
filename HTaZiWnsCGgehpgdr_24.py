
def license_plate(s, n):
  t=s.upper().split('-')
  t=''.join(t)[::-1]
  out=[]
  
  while len(t)>0:
    out.append(t[:n])
    t=t[n:]
  
  return '-'.join(out)[::-1]

