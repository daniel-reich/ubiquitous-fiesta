
def left_digit(string):
  for char in string:
    if char.isdigit():
      return int(char)
      break

