
def highest_digit(num):
  number = []
  for i in str(num):
    number.append(int(i))
  return max(number)

