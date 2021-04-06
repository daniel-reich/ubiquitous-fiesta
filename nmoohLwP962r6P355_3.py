
def straight_digital(number):
  a = 1
  if number < 0:
    number = abs(number)
    a = -1
  n = [int(x) for x in str(number)]
  n[0] = n[0]*a
  if len(n) < 3:
    return 'Not Straight'
  if sum(n)//len(n) == n[0]:
    return 'Trivial Straight'
  check = n[1]-n[0]
  for i in range(2,len(n)):
    if n[i]-n[i-1] != check:
      return 'Not Straight'
  return check

