
def recaman(n):
  
  l = []
  d = []
  s = set()
  d_val=set()
  
  for i in range(0,n):
    if i>0:
      val = l[i-1]-i
      if val not in s and val>0:
        l.append(l[i-1]-i)
        s.add(l[i-1]-i)
      else:
        val = l[i-1]+i
        l.append(val)
        if val in s:
          if val not in d_val:
            d.append(val)
            d_val.add(val)
        else:
          s.add(val)
      
    else:
      l.append(0)
  
  return "---> Recaman's sequence: " +str(l)+ "\n---> Duplicates for n = "+str(n)+": "+str(d)

