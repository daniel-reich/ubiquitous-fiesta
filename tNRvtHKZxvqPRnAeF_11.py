
def digit_occurrences(start, end, digit):
  su = 0
  a = 0
  aa = [str(x) for x in range(start,end+1)]
  for x in aa:
    a = x.count(str(digit))
    su += a
    a = 0
  return su

