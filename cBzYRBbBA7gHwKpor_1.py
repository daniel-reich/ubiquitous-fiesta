
def secret_password(m):
  if len(m)==9and all('a'<=x<='z'for x in m):
    l=list(m)
    l[0],l[2]=str(ord(l[0])-96),str(ord(l[2])-96)
    l[3],l[5]=l[5],l[3]
    l[6:9]=[('a',chr(ord(x)+1))[x!='z']for x in l[6:9]]
    return''.join(l[3:6]+l[6:9]+l[0:3])
  return'BANG! BANG! BANG!'

