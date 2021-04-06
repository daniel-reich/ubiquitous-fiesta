
def row_sum(n):
  num = 0
  for i in range(1,n+1):
    num += i
  return sum(range(num-n+1,num+1))

