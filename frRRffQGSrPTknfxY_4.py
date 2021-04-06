
def digit_count(n):
  n = str(n)
  new_int = ""
  for digit in n:
    digit_count = 0
    for x in n:
      if digit == x:
        digit_count += 1
    new_int += str(digit_count)
  return int(new_int)

