
def digit_occurrences(start, end, digit):
  return "".join(str(n) for n in range(start,end+1)).count(str(digit))

