
def ascii_sort(lst):
  sum1=0
  sum2=0
  for x in lst[0]:
    sum1+=ord(x)
  for x in lst[1]:
    sum2+=ord(x)
  return lst[0] if sum1<sum2 else lst[1]

