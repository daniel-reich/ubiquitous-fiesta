
def boxes(weights):
  total=0
  count=0
  for i in weights:
    total+=i
    if total>10:
      total=i
      count+=1
    if total>9:
      count+=1
      total=0
  return count+1 if total else count

