
def mean(num):
  sum = 0
  numstr = str(num)
  ndig = len(numstr)
  for digit in numstr:
    d = int(digit)
    sum = sum+d
  avg = sum/ndig
  return(avg)

