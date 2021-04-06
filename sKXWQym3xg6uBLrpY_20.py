
def iqr(lst):
  lst.sort()
  if len(lst)%2 == 0:
    if len(lst)%4 == 0:
      hlv = int(len(lst)/2)
      st = int((len(lst)/4)-1)
      q1so = slice(st,st+2)
      q1 =sum(lst[q1so])/2
      q3so = slice(st+hlv,st+2+hlv)
      q3 = sum(lst[q3so])/2
    else:
      hlv = int(len(lst)/2)
      st = int((len(lst)/4))
      q1so = slice(st,st+1)
      q1 = sum(lst[q1so])
      q3so = slice(st+hlv,st+hlv+1)
      q3 = sum(lst[q3so])
  elif (len(lst)+1)%4 == 0:
    hlv = int(len(lst)/2)
    st = int((len(lst)/4))
    q1so = slice(st,st+1)
    q1 = sum(lst[q1so])
    q3so = slice(st+hlv+1,st+hlv+2)
    q3 = sum(lst[q3so])
  else:
    hlv = int(len(lst)/2)
    st = int((len(lst)/4)-1)
    q1so = slice(st,st+2)
    q1 = sum(lst[q1so])/2
    q3so = slice(st+hlv+1,st+3+hlv)
    q3 = sum(lst[q3so])/2
  return (q3-q1)

