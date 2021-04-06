
def block(lst):
  count=[]
  val=0
  h = 0
  switch = False
  for n in range(len(lst[0])):
    for l in range(len(lst)):
      if l==len(lst)-1:
        if switch==True:
          val+=1
          switch=False
          count.append(val)
          val=0
          break
        else:
          count.append(val)
          val=0
          break
      if lst[l][n] == 2:
        switch=True
        continue      
      if switch==True:
        val+=1
        continue
  for c in count:
    h=h+c
  return h

