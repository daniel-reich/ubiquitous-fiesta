
def score_it(s):
  v=""
  c=0
  f=0
  p="abcdefghijklmnopqrstuvwxyz"
  for t in s:
    if t!="(" and t!=")" and t not in p:
      v=v+t
    elif t =="(":
      if len(v)>0:
        f=f+(int(v)*c)
        v=""
      c+=1
    elif t==")":
      if len(v)>0:
        f=f+(int(v)*c)
        v=""
      c-=1
  return f

