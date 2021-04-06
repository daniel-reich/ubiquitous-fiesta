
def straight_digital(number):
  print(number)
  if number < 100:
    return 'Not Straight'
  ints = []
  for char in str(number):
    ints.append(int(char))
  diff = ints[1] - ints[0]
  for i in range(len(ints)-1):
    if ints[i+1] - ints[i] != diff:
      return 'Not Straight'
  if diff == 0:
    return 'Trivial Straight'
  return diff

