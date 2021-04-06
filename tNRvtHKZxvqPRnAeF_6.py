
def digit_occurrences(start, end, digit):
  count = 0;
  for i in range(start, end+1):
    for j in str(i):
      if j != '-' and int(j) == digit:
        count += 1
  return count

