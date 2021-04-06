
def unmix(txt):
  li=list() 
  for i in range(0,len(txt)-1,2):
    for j in range(i+1,len(txt),2):
      li.append(txt[j])
      break
    li.append(txt[i])
  if(len(txt)%2!=0):
    li.append(txt[-1])
  return (''.join(li))

