
def sum_odd_and_even(lst):
  sum_even=0
  sum_odd=0
  result=[]
  for i in lst:
    if i%2==0:
      sum_even=sum_even+i
    else:
      sum_odd=sum_odd+i
  result.append(sum_even)
  result.append(sum_odd)
  return result

