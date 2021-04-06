
def digit_occurrences(start, end, digit):
  total = 0
  for i in range(start,end+1):
    total+=str(i).count(str(digit))
  return total

