
def duplicate_count(txt):
  dicty=dict()
  counter=0
  for i in txt:
    dicty[i]=dicty.get(i, 0)+1
  for key,val in dicty.items():
    if val>=2:
      counter+=1
  return counter

