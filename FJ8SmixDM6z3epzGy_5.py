
def check_perfect(num):
  sum = 0
  index = 1
  while index < num:
    if num % index == 0:
      sum += index
    index += 1
  if sum == num:
    return True
  else:
    return False

