
def safecracker(start, inc):
  first = (start - inc[0])%100
  second = (first + inc[1])%100
  third = (second - inc[2])%100
  return [first,second,third]

