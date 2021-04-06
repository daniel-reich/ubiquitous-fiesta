
def split(txt):
  
  temp,res="",[]
  counter,i=0,0
  while i<len(txt):
    temp+=txt[i]
    if txt[i]=="(":
      counter+=1
    elif txt[i]==")":
      counter-=1
    
    if counter==0:
      res.append(temp)
      temp=""
    i+=1
  return res

