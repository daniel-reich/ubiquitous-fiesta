
def is_equal(lst):
  sum1, sum2 = 0, 0
  while lst[0] > 0:
    sum1 += lst[0]%10
    lst[0] = int(lst[0]/10)
  while lst[1] > 0:
    sum2 += lst[1]%10
    lst[1] = int(lst[1]/10)
  return sum1 == sum2

