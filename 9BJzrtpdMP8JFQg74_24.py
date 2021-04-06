
def twins(lst):
  sum1 = sum2 = 0
  for x in range(len(lst)):
    for j in range(x+1):
      sum1+=lst[j]
    for i in range(x+1,len(lst)):
      sum2+=lst[i]
    if(sum1 == sum2):
      return x+1
    else:
      sum1 = sum2 = 0

