
def sum_digits(n):
  count=0
  if n==0:
    return 1
  while n!=0:
    n//=10
    count+=1
  return count

