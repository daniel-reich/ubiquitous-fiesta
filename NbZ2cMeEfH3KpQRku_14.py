
def portion_happy(n):
  h0,h1=0,0
  if n.count(0)==0 or n.count(1)==0:
    return 1
  else:
    n.insert(0,'*');n.append('*')
    for x in range(1,len(n)-1):
      if n[x-1]==n[x] or n[x+1]==n[x]:
        if n[x]==0:
          h0 += 1
        else:
          h1 += 1
  n = n[1:-1]
  return round((h0+h1)/len(n),1)

