
def left_digit(num):
  string = [i for i in num if i.isnumeric()]
  return int(string[0])

