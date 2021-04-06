
def split(number):
  if number == 1:
    return 1
  if number == 2:
    return 2
  max_threes = number // 3
  threes = max_threes if (number % 3) % 2 == 0 else max_threes - 1
  twos = (number - threes*3) / 2
  return 3**threes * 2**twos

