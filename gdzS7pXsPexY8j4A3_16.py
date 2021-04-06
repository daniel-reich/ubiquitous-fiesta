
def count_digits(lst, t):
  output = []
  for digit in lst:
    total = 0
    digit = str(digit)
    if t == 'even':
      for i in digit:
        if int(i) % 2 == 0:
          total += 1
    else:
      for i in digit:
        if int(i) % 2 != 0:
          total += 1
    output.append(total)
  return output

