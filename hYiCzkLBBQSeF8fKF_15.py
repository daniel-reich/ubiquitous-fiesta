
def count(deck):
  a=0
  for i in deck:
    if i in range(2,7):
      a+=1 
    if i==10 or type(i) == str:
      a-=1
  return a

