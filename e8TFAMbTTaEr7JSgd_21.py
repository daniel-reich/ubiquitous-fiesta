
def left_digit(num):
  for char in num:
    if char.isdigit():
      return int(char)

