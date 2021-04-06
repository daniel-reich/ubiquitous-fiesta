
def edit_words(l):
  r=[]
  for x in l:
    s,p=x[::-1].upper(),len(x)//2+(0,1)[len(x)%2]
    r.append(s[:p]+'-'+s[p:])
  return r

