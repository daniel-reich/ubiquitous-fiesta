
def pilish_string(txt):
  lst = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
  if txt=='': return ''
  res=[txt[0]]
  count =0  
  for x in txt[1:sum(lst)]:     
    if len(res[-1])< lst[count]:res[-1]+=x
    else:
      res.append(x)
      count+=1    
  while len(res[-1])!= lst[count]:    
    res[-1]+= res[-1][-1]
  return ' '.join(res)

