
def group_seats(lst, n):
  c=0
  d=0
  switch=False
  for l in lst:
    if switch==True:
      c=0
    for m in range(len(l)):
      switch=True
      if l[m]==0:
        c+=1
        if m==len(l)-1:
          if c==n:
            d+=1
          elif c>n:
            d=d+(c//n)+1
      else:
        if c==n:
          d+=1
        elif c>n:
          d=d+(c//n)+1
        c=0
  return d

