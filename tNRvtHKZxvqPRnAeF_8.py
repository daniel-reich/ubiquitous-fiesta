
def digit_occurrences(start, end, digit):
  c = 0
  for i in range(start, end+1):
    i = str(i)
    for j in i:
      if str(digit) == j:
        c += 1
  return c

