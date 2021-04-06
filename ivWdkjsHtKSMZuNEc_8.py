
def find_shortest_words(txt):
  txt=txt.lower()
  lst=[]
  temp=""
  for i in txt:
    if i.isalpha() or i=="'":
      temp+=i
    else:
      if temp=="":
        continue
      lst.append(temp)
      temp=""
  if temp!="": 
    lst.append(temp)
  new=[]
  min=len(lst[0])
  for i in lst:
    if len(i)<=min:
      min=len(i)
  
  for i in lst:
    if len(i)==min:
      new.append(i)
  new.sort()
  return new

