
def no_strangers(txt):
  lst1=[];lst2=[]
  word=''.join(c if c.isalnum() or c=="'" else ' ' for c in txt.lower()).split()
  for i in set(word):
    if word.count(i)>=5:lst2+=[i]
    elif word.count(i)>=3:lst1+=[i]
  for i in lst1:
    for j in range(2):word.remove(i)
  for i in lst2:
    for j in range(4):word.remove(i)
  return [sorted(lst1,key=word.index),sorted(lst2,key=word.index)]

