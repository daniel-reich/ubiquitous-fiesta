
def partitions(n):
  if n == 0:
    return 1
  output = 0
  k = 1
  prev_n = n - ((k*((3*k)-1))/2)
  while prev_n >= 0:
    output += ((-1)**(k+1))*partitions(prev_n)
    if k > 0:
      k = -k
    else:
      k = -k + 1
    prev_n = n - ((k*((3*k)-1))/2)
  return output

