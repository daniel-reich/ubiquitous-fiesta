
def count_ones(lst):
  count=0
  consec=0
  for num in lst:
    if num==1:
      count+=1
    if num==0:
      if count>1: consec+=1
      count=0
  if count>1: consec+=1
  return consec

