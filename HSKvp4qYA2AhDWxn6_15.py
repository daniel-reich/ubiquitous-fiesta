
def total_points(guesses, word):
  a=guesses
  y=[]
  o=[]
  count=0
  x=word
  for i in a:
    for j in i:
      if x.count(j)>=i.count(j):
        y.append(i)
  for i in y:
    if i not in o and y.count(i)==len(i):
      o.append(i)
  for i in o:
    if len(i)==3:
      count+=1
    if len(i)==4:
      count+=2
    if len(i)==5:
      count+=3
    if len(i)==6:
      count+=54
  return(count)

