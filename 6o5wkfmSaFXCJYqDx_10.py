
def abcmath(a, b, c):
  number = a
  i = 1
  while i <= b:
    number = number + number
    i += 1
  if number % c == 0:
    return True
  else:
    return False

