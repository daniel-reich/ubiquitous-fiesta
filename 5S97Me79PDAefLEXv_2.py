
def lambda_to_def(c):
  f,b=c.strip().split(':',1)
  if'"'in f or"'"in f:
    c=c.strip().split(':')
    f,b=c[0]+':'+c[1],c[2]
  f,p=f.strip().split('=',1)
  f,p,b=f.strip(),p.strip(),b.strip()
  i=p.find(' ')
  p=p[i+1:]if i>=0else''   
  return"def %s(%s):\n\treturn %s"%(f,p,b)

