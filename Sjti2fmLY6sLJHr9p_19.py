
def calcNextGen(gen):
  text=list(str(gen))
  number=text[0]
  count=0
  newtext=[]
  i=0
  securite=0
  while(i<len(text) or securite>1000000):
    securite+=1
    while(text[i]==number):
      count+=1
      i+=1
      if(i>=len(text)):
        break
    newtext.append(str(count))
    newtext.append(str(number))
    count=0
    if(i>=len(text)):
      break
    else:
      number=text[i]
  s=map(str,newtext)
  s=''.join(s)
  s=int(s)
  return s
def look_and_say(start, n):
  l=[]
  newgen=start
  l.append(newgen)
  for i in range(n-1):
    newgen=calcNextGen(newgen)
    l.append(newgen)
  return l

