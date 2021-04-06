
def digit_occurrences(start, end, digit):
  count = 0
  for x in range(start,end+1):
    count += str(x).count(str(digit))
  return count

