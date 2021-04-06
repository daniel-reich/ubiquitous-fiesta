
def dlen(num):
  return len(str(num))
​
def decrease_to_next_digit(number):
  num_digits = dlen(number)
  next_num_str = (num_digits-1)*"9"
  if next_num_str == "":
    return 0
  return int(next_num_str)
​
def digits(number):
  number = number-1
  total = 0
  while number > 0:
    num_digits = dlen(number)
    next_number = decrease_to_next_digit(number)
    diff = number - next_number
    total += diff*num_digits
    number = next_number
  return total

