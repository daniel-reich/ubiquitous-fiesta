
def almost_sorted(lst):
  count_1=0
  count_2=0
  magic=0
  i=1
  while i<len(lst):
    if (lst[i-1]<lst[i]): 
      count_1+=0
    else:
      count_1+=1
    i+=1
  i=1
  while i<len(lst):
    if lst[i-1]>lst[i]:
      count_2+=0
    else:
      count_2+=1
    i+=1
    
      
  if count_1==1 or count_2==1:
    magic=True
  else:
    magic=False
  return(magic)

