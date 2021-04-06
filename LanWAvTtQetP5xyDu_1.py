
def coins_div(lst):
  trg=sum(lst)//3
  p=[trg,trg,trg]
  for i in sorted(lst,reverse=True):
    if not i-p[0]:p[0]-=i
    elif not i-p[1]:p[1]-=i
    elif not i-p[2]:p[2]-=i
    else:p[2]-=i
    p.sort()
  return p[0]==p[2]

