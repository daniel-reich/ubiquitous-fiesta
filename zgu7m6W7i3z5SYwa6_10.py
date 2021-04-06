
def is_equal(lst):
  lst1 = [i for i in str(lst[0])]
  lst2 = [i for i in str(lst[1])]
  sum1=0
  sum2=0
  for i in lst1:
    sum1 = sum1+int(i)
  for i in lst2:
    sum2 = sum2+int(i)
  if sum1==sum2:
    return True
  else:
    return False

