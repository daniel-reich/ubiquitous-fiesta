
def digit_occurrences(start, end, digit):
  digit = str(digit)
  count = 0
  for i in range(start,end+1):
    x = str(i)
    count += x.count(digit)
  return count

