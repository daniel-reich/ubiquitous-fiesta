
def shared_letters(txt1, txt2):
  count1=0
  count2=0
  a=[txt2.count(i) for i in txt1]
  for j in a:
    if j>0:
      count1+=1
  b=[txt1.count(i) for i in txt2]
  for j in b:
    if j>0:
      count2+=1       
  return min(count1,count2)

