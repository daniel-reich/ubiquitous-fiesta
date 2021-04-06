
def digit_occurrences(start, end, digit):
  return sum([[y for y in str(x)].count(str(digit)) for x in range(start,end+1)])

