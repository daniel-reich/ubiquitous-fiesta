
def join(lst):
  l=len(lst)
  ans='';min=l
  for i in range(l-1):
    s=lst[i]
    for j in range(len(lst[i])-1,0,-1):
      if lst[i][j:] in lst[i+1]:
        s=lst[i][:j]
    m=len(lst[i])-len(s)
    if m<min:min=m
    ans+=s
  return [ans+lst[-1],min]

