
def straight_digital(number):
  if number < 100:
    return 'Not Straight'
  s = str(number)
  diff = [int(s[i]) - int(s[i - 1]) for i in range(1, len(s))]
  if len(set(diff)) == 1:
    if diff[0] == 0:
      return 'Trivial Straight'
    else:
      return diff[0]
  return 'Not Straight'

