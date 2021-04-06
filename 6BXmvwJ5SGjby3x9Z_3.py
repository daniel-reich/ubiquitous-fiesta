
def hours_passed(a,b):
  if a==b: return 'no time passed'
  c,d=int(a.split(':')[0]),int(b.split(':')[0]) 
  e,f=a[-2],b[-2]
  if c==12 and e=='A': c=0
  if e=='P': c+=12
  if d==12 and f=='A': d=0
  if f=='P': d+=12
  return str(d-c)+' hours'

