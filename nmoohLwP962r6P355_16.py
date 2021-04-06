
def straight_digital(number):
  if number < 100:
    return "Not Straight"
  number = str(number)[::-1]
  if number.count(number[0]) == len(number):
    return "Trivial Straight"
  step = ord(number[0]) - ord(number[1])
  for foo in range(1, len(number) - 1):
    if (ord(number[foo]) - ord(number[foo + 1])) != step:
      return "Not Straight"
  return step

